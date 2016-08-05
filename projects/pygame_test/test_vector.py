from gameobjects.vector2 import *

A = (10.0, 35.0)
B = (20.0, 10.0)
AB = Vector2.from_points(A, B)

print "AB is ", AB
print "AB *2 is ", AB * 2
print "AB /2 is ", AB / 2
print "AB +(10,5) is ", AB + (10, 5)
print "Magnitude of AB is ", AB.get_magnitude()
print "AB normalized is ", AB.get_normalised()