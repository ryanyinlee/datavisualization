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
            xsteps = self.get_steps()
            ysteps = self.get_steps()

            if xsteps == 0 and ysteps == 0:
                continue

            x = self.xvals[-1] + xsteps
            y = self.yvals[-1] + ysteps
            
            self.xvals.append(x)
            self.yvals.append(y)
    
    def get_steps(self):
        """Determine direction and distance for each step"""
       
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        steps = distance * direction
        return steps
            
        


