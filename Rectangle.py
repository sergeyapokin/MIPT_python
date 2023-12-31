from abc import ABC, abstractmethod
from Figure import Figure
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse


class Rectangle(Figure):
    def __init__(self, points):
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()

    def calculatePerimeter(self):
        return 2 * (self.points[1][0] - self.points[0][0]) + 2 * (self.points[1][1] - self.points[0][1])

    def calculateSquare(self):
        return (self.points[1][0] - self.points[0][0]) * (self.points[1][1] - self.points[0][1])

    def __str__(self):
        s=''
        s+='"rectangle"'
        s+= ';'
        s+=str(self.calculateSquare())
        s+= ';'
        s+=str(self.calculatePerimeter())
        s+=';('
        s+=str(self.points[0][0])
        s+=':'
        s+=str(self.points[0][1])
        s+=');('
        s+=str(self.points[1][0])
        s+=':'
        s+=str(self.points[1][1])
        s+=')'
        return s

    def constructFromSeries(cls,series: pd.Series):
        points = tuple((tuple(series.iloc[1:3])[0].split(':'), series.iloc[2]))
        return cls(points)

    def graphFigure(self):
        fig, ax = plt.subplots()
        ax.set_xlim(- self.points[0][0] - (self.points[1][0] - self.points[0][0]), self.points[1][0] + (self.points[1][0] - self.points[0][0]))
        ax.set_ylim(- self.points[0][1] - (self.points[1][1] - self.points[0][1]), self.points[1][1] + (self.points[1][1] - self.points[0][1]))
        ax.add_patch(plt.Rectangle(self.points[0], (self.points[1][0] - self.points[0][0]), (self.points[1][1] - self.points[0][1])))
        ax.set_aspect(1)
        plt.show()
