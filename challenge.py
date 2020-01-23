import math
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(self.x**2 + self.y**y)
        
    def plus(self, newVec):
        vec = Vec(self.x + newVec.x, self.y + newVec.y)
        return vec
        
    def minus(self, newVec):
        vec = Vec(self.x - newVec.x, self.y - newVec.y)
        return vec
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
        
        
        
        
        