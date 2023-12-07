from abc import ABC, abstractmethod
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class Ellipse(Figure):
  def __init__(self, points):
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()

  def calculatePerimeter(self):
        return 4 * (math.pi * self.points[1] * self.points[2] + self.points[1] - self.points[2])/(self.points[1] + self.points[2])


  def calculateSquare(self):
        return math.pi * self.points[1] * self.points[2]

  def __str__(self):
        s=''
        s+='"ellipse"'
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
        s+= ';'
        s+=str(self.points[2])
        return s

  def constructFromSeries(cls,series: pd.Series) -> object:
        points = (tuple(map(float, series[1].split(':'))), series[2], series[3])
        return cls(points)

  def graphFigure(self):
        fig, ax = plt.subplots()
        ax.set_xlim(- self.points[0][0] - self.points[1]*2, self.points[0][0] + self.points[1]*2)
        ax.set_ylim(- self.points[0][1] - self.points[2]*2, self.points[0][1] + self.points[2]*2)
        ax.add_patch(plt.ellipse(self.points[0], self.points[1], self.points[2], 0))
        #угол наклона эллипса не задан, пусть будет 0
        ax.set_aspect(1)
        plt.show()
