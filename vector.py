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

