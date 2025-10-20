# An example of studying the motion of a particle in one
# dimension under an elastic force.

import math

# Set up parameters and arrays
n = 100001; j = 500
x = [0]*n; v = [0]*n

# Assign time step and initial position and velocity
dt = 2*math.pi/(n-1)
x[0] = 0; v[0] = 1

# Calculate other position and velocity recursively
for i in range(n-1):
    x[i+1] = x[i]+v[i]*dt
    v[i+1] = v[i]-x[i]*dt

# Output the result in every j time steps
jdt = j*dt
t = 0
for i in range(0, n, j):
    print(t, x[i], v[i])
    t += jdt
