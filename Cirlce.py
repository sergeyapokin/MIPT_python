
class Circle(Figure):
    def __init__(self, points):
        self.points =  points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()

    def calculatePerimeter(self):
        return math.pi*2*self.points[1]

    def calculateSquare(self):
        return math.pi*self.points[1]*self.points[1]

    def __str__(self):
        s=''
        s+='"circle"'
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

    @classmethod
    def constructFromSeries(cls,series: pd.Series) -> object:
        points = tuple((tuple(series.iloc[1:3])[0].split(':'), series.iloc[2]))
        print(points)
        return cls(points)

    def graphFigure(self):
        fig, ax = plt.subplots()
        ax.set_xlim(- self.points[0][0] - self.points[1]*3, self.points[0][0] + self.points[1]*3)
        ax.set_ylim(- self.points[0][1] - self.points[1]*3, self.points[0][1] + self.points[1]*3)
        ax.add_patch(plt.Circle(self.points[0], self.points[1]))
        ax.set_aspect(1)
        plt.show()