class Rectangle:
    def __init__(self,x,y,widht,height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height

    def __str__(self):
        return f"Rectangle: {self.x}, {self.y}, {self.widht}, {self.height}"

    def getArea(self):
        return self.widht*self.height

rec = Rectangle(5, 10, 50, 100)

print(rec)
print(rec.getArea())