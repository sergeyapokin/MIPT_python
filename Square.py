from abc import ABC, abstractmethod
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse


class Square(Figure):
    def __init__(self, points):
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()

    def calculatePerimeter(self):
        return 4 * self.points[1]

    def calculateSquare(self):
        return self.points[1]**2

    def __str__(self):
        s=''
        s+='"square"'
        s+= ';'
        s+=str(self.calculateSquare())
        s+= ';'
        s+=str(self.calculatePerimeter())
        s+=';('
        s+=str(self.points[0][0])
        s+=':'
        s+=str(self.points[0][1])
        s+=');'
        s+=str(self.points[1])
        return s

    def constructFromSeries(cls,series: pd.Series):
        points = (tuple(series.iloc[1:2])[0].split(':'), float(series.iloc[2]))
        return cls(points)


    def graphFigure(self):
        fig, ax = plt.subplots()
        ax.set_xlim(- self.points[0][0] - self.points[1], self.points[0][0] + 2 * self.points[1])
        ax.set_ylim(- self.points[0][1] - self.points[1], self.points[0][1] + 2 * self.points[1])
        ax.add_patch(plt.Rectangle(self.points[0], self.points[1], self.points[1]))
        ax.set_aspect(1)
        plt.show()
