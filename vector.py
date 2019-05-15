import math
class Vector():
    def __init__(self,coordinates):
        self.coordinates = coordinates
        try:
            if coordinates:
                self.coordinates = tuple(coordinates)
                self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an itearable')

    def __str__(self):
        print(self.coordinates)
        return 'Vector:{}'.format(self.coordinates)

    def __eq__(self,v):
        return self.coordinates == v.coordinates

    # The magnitude of a vector is the length of the vector
    def magnitude(self):
        return math.sqrt(sum(i*i for i in self.coordinates))
    # Direction 
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise except('Cannot normalize the zero vector')
        
v1 = Vector([-0.221,7.437])
v2 = Vector([8.813,-1.331,-6.247])
v3 = Vector([5.581,-2.136])
v4 = Vector([1.996,3.108,-4.554])
print(v1.magnitude())
print(v2.magnitude())
print(v3.magnitude())
print("v4 of direction:{}".format(v4.direction()))