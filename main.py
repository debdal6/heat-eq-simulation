import numpy
import matplotlib.pyplot as pyPlot

# Global Constants

lengthOfRod = 100 #n
unitTime = 10 #m
heatConductivity = 385
xVectorStepSize = 1 #h
yVectorStepSize = 1 #k

# Length Vector plotted on x-axis
xVector = numpy.arange(0, lengthOfRod+xVectorStepSize, xVectorStepSize)
# Time Vector plotted on y-axis
yVector = numpy.arange(0, unitTime+yVectorStepSize, yVectorStepSize)

boundaryConditions = [1084, 1084]
intialConditions = numpy.sin(numpy.pi*xVector)

# Empty Matrix/NestedList with zeroes
gridMatrix = numpy.zeros((lengthOfRod, unitTime))
gridMatrix[0,:] = boundaryConditions[0]
gridMatrix[-1,:] = boundaryConditions[1]
gridMatrix[:, 0] = intialConditions

for deltaTime in range (1, unitTime-1):
    for deltaLength in range (1, lengthOfRod-1):
        gridMatrix[deltaLength,deltaTime]=(
            (
                (heatConductivity*deltaTime-1)/deltaLength**2)*
                (gridMatrix[deltaLength-1,deltaTime-1]-
                 2*gridMatrix[deltaLength,deltaTime-1]+
                 gridMatrix[deltaLength+1,deltaTime-1])
            ) + gridMatrix[deltaLength,deltaTime-1]

print(gridMatrix)

pyPlot.plot(gridMatrix)
pyPlot.show()