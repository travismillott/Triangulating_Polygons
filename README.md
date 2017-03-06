# Triangulating_Polygons

## My solution

I opted for a recursive function that would search for potential solutions.  The function searches all possible color combinations for a given graph, in search of a potential solution.  It's optimized in such a way that it will search each branch of potential solutions tree until it finds more than 2 complete triangles, then it moves on to another branch.  If it finds a solution it stops and returns True.  It takes about 5 minutes to find that there is no solution with exactly 2 complete triangles.

## Resources

I googled a bit, but couldn't find any more information relating to the specifics of this problem.  So I opted to solve it on my own using what I already knew about graphs.

## Time

I estimated that it might take me between 2-4 hours.  It took me about 2 hours to code it, and another hour to write up the documentation and do a little refactoring.

## What I would improve

If I could do this again, I'd try to think up a way to optimize my solution so that it can solve the problem faster.

## How to run
The graph is defined within main.py, so all you need to do is run `python2.7 main.py`
