# -*- coding: utf-8 -*-
"""Quadrilateral.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U_eS1ch-fDyxAIsCZvOoMm4jioLrxFn
"""

from abc import ABC, abstractmethod
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Quadrilateral(Figure):
    def __init__(self, points):
        self.points = points
        self.side_1 = math.sqrt((self.points[1][0] - self.points[0][0])**2 + (self.points[1][1] - self.points[0][1])**2)
        self.side_2 = math.sqrt((self.points[2][0] - self.points[1][0])**2 + (self.points[2][1] - self.points[1][1])**2)
        self.side_3 = math.sqrt((self.points[3][0] - self.points[2][0])**2 + (self.points[3][1] - self.points[2][1])**2)
        self.side_4 = math.sqrt((self.points[0][0] - self.points[3][0])**2 + (self.points[0][1] - self.points[3][1])**2)
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()

    def calculatePerimeter(self):
         return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def calculateSquare(self):
        side_5 = math.sqrt((self.points[2][0] - self.points[0][0])**2 + (self.points[2][1] - self.points[0][1])**2)
        P_1 = side_5 + self.side_1 + self.side_2
        S_1 = math.sqrt(P_1*(P_1 - side_5)*(P_1 - self.side_1)*(P_1 - self.side_2))
        P_2 = side_5 + self.side_3 + self.side_4
        S_2 = math.sqrt(P_1*(P_1 - side_5)*(P_1 - self.side_3)*(P_1 - self.side_4))
        return S_1 + S_2

    def __str__(self):
        s=''
        s+='"quadrilateral"'
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
        s+=');('
        s+=str(self.points[2][0])
        s+=':'
        s+=str(self.points[2][1])
        s+=');('
        s+=str(self.points[3][0])
        s+=':'
        s+=str(self.points[3][1])
        return s

    def constructFromSeries(cls,series: pd.Series):
        points = (tuple(series.iloc[1:2])[0].split(':'), float(series.iloc[2]))
        return cls(points)


    def graphFigure(self):
        fig, ax = plt.subplots()
        ax.set_xlim(- self.points[0][0] - self.perimeter/4, self.points[0][0] + self.perimeter/2)
        ax.set_ylim(- self.points[0][1] - self.perimeter/4, self.points[0][1] + self.perimeter/2)
        ax.add_patch(plt.Polygon(self.points))
        ax.set_aspect(1)
        plt.show()