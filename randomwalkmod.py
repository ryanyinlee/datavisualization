from random import choice

class RandomWalk:
    """Generates random walks"""

    def __init__(self, numpoints=5000):
        """Initialize attributes of a walk"""
        self.numpoints = numpoints

        self.xvals = [0]
        self.yvals = [0]
    
    def create_walks(self):
        """Randomly creates the walkpoints and fills the lists in init"""
        while len(self.xvals) < self.numpoints:
            xdirection = choice([1, -1, 0])
            xdistance = choice([0,1,2,3,4,5,6,7,8,9])
            xsteps = xdistance * xdirection

            ydirection = choice([1,-1])
            ydistance = choice([0,1,2,3,4])
            ysteps = ydistance * ydirection

            if xsteps == 0 and ysteps == 0:
                continue

            x = self.xvals[-1] + xsteps
            y = self.yvals[-1] + ysteps
            
            self.xvals.append(x)
            self.yvals.append(y)

