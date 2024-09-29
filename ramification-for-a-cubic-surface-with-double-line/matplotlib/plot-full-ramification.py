import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid

delta = 0.01
xrange = arange(-2.0, 2.0, delta)
yrange = arange(-2.0, 2.0, delta)
x, y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
Daffine =  - 16 * x**4 + 11 * x**2 * y**2 - 2 * y**4 - 18 * x**2 * y + 6 * y**3 + 3 * x**2 - 6 * y**2 + 2 * y

# Step 1. plotting circle
matplotlib.pyplot.contour(x, y, Daffine , [0])


# Step 2. plotting  the image of the double line
line  = y
matplotlib.pyplot.contour(x, y, line, [0])

matplotlib.pyplot.savefig('output.png', dpi=300, bbox_inches='tight' )
matplotlib.pyplot.show()


