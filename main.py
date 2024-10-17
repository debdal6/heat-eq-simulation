import numpy
import matplotlib.pyplot as pyPlot

# Global Constants

lengthOfRod = 1 #n
unitTime = 0.1 #m
heatConductivity = 1
xVectorStepSize = 0.25
yVectorStepSize = 0.025

# Length Vector plotted on x-axis
xVector = numpy.arange(0, lengthOfRod+xVectorStepSize, xVectorStepSize)
# Time Vector plotted on y-axis
yVector = numpy.arange(0, unitTime+yVectorStepSize, yVectorStepSize)

boundaryConditions = [0, 0]
intialConditions = numpy.sin(numpy.pi*xVector)

xVectorLength = len(xVector)
yVectorLength = len(yVector)

# Empty Matrix/NestedList with zeroes
gridMatrix = numpy.zeros((xVectorLength, yVectorLength))
gridMatrix[0,:] = boundaryConditions[0]
gridMatrix[-1,:] = boundaryConditions[1]
gridMatrix[:, 0] = intialConditions

for deltaTime in range (1, yVectorLength-1):
    for deltaLength in range (1, xVectorLength-1):
        gridMatrix[deltaLength,deltaTime]=(
            (
                (heatConductivity*(deltaTime-1))/deltaLength**2)*
                (gridMatrix[deltaLength-1,deltaTime-1]-
                 2*gridMatrix[deltaLength,deltaTime-1]+
                 gridMatrix[deltaLength+1,deltaTime-1])
            ) + gridMatrix[deltaLength,deltaTime-1]

print(gridMatrix)

pyPlot.plot(gridMatrix)
pyPlot.show()