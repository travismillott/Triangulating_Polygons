#
# Drivewyze programming challenge
#
# Prints whether or not there is a solution to the Triangulating Polygons problem.

import copy

# Vertices + edges mapping
VERTICES = {'A': 'BLK',
            'B': 'ALMC',
            'C': 'BMND',
            'D': 'CNE',
            'E': 'DNTVF',
            'F': 'EVUG',
            'G': 'FUH',
            'H': 'GUSI',
            'I': 'JQSH',
            'J': 'KOPQI',
            'K': 'ALOJ',
            'L': 'ABMOK',
            'M': 'LBCNTRO',
            'N': 'MCDET',
            'O': 'JKLMRP',
            'P': 'JORQ',
            'Q': 'JPRSI',
            'R': 'QPOMTS',
            'S': 'IQRTUH',
            'T': 'SRMNEVU',
            'U': 'STVFGH',
            'V': 'TEFU',
            }

ALREADY_COLORED_VERTICES = {'A':'red',
                            'B':'red',
                            'C':'yellow',
                            'D':'blue',
                            'E':'red',
                            'F':'yellow',
                            'G':'blue',
                            'H':'red',
                            'I':'red',
                            'J':'yellow',
                            'K':'blue',
                            }

COLORS = ['red','blue','yellow']

NUM_COMPLETE_TRIANGLES = 2


class Vertex(object):
    def __init__(self, name, edges, color):
        self.name  = name
        self.edges = edges
        self.color = color


def are_connected(vertex1, vertex2):
    return vertex2.name in vertex1.edges


def different_colors(color1, color2, color3):
    # Verify that colors exist for each vertex, and that they are not the same
    return color1 in COLORS and color2 in COLORS and color3 in COLORS and \
           color1 != color2 and color2 != color3 and color1 != color3


def num_new_complete_triangles(found_triangles, vertices, vertex):
    # Checks for any new triangles to add to the found_triangles list of triangle vertices
    # New complete triangles must:
    #           Have different colored edges
    #           Have connected edges
    #           Not already be in the found_triangles list
    for edge1 in vertex.edges:
        for edge2 in vertex.edges:
            if edge1 == edge2: continue
            if different_colors(vertex.color, vertices[edge1].color, vertices[edge2].color) \
                    and are_connected(vertices[edge1], vertices[edge2]) \
                    and {vertex.name, edge1, edge2} not in found_triangles:
                found_triangles.append({vertex.name, edge1, edge2})
    return found_triangles


def count_triangles(vertices):
    # Counts the number of triangles in a given graph of vertices
    found_triangles = []
    for vertex in vertices:
        found_triangles = num_new_complete_triangles(found_triangles, vertices, vertices[vertex])
    return found_triangles


def find_solution_with_complete_triangles(vertices):
    # Recursive function to find potential solutions with exactly NUM_COMPLETE_TRIANGLES
    if len(count_triangles(vertices)) > NUM_COMPLETE_TRIANGLES:
        # Stop going down this branch of potential solutions because we already have > NUM_COMPLETE_TRIANGLES
        return False

    uncolored_vertexes_left = [vertex for vertex in vertices.values() if not vertex.color]
    if len(uncolored_vertexes_left) == 0 and len(count_triangles(vertices)) == NUM_COMPLETE_TRIANGLES:
        # Found a solution, graph is fully colored in, and we have the right number of complete triangles
        return True

    for vertex in vertices.values():
        if not vertex.color:
            for color in COLORS:
                # Try the graph with all colors for all uncolored vertices
                vertex.color = color
                if find_solution_with_complete_triangles(copy.deepcopy(vertices)):
                    return True
    return False


def main():
    vertices = {}
    # Create the graph from the VERTICES and ALREADY_COLORED_VERTICES dictionaries
    for vertex, edges in VERTICES.items():
        color = ALREADY_COLORED_VERTICES.get(vertex)
        vertices[vertex] = Vertex(vertex, edges, color)

    print 'Searching for solution...'
    # Call recursive function to find any potential solution
    print 'SOLUTION POSSIBLE:'+ str(find_solution_with_complete_triangles(vertices))


if __name__ == '__main__':
    main()
