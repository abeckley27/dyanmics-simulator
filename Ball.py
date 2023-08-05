import math

class Ball(object):

    def __init__(self, pos_x, pos_y, dx, dy, r, c):
        self.x = pos_x
        self.y = pos_y
        self.vx = dx
        self.vy = dy
        self.radius = r
        self.color = c

    def __str__(self):
        return str(self.x)+str(self.y)+str(self.radius) + self.color

    def position(self):
        return (self.x, self.y)

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def get_color(self):
        return self.color

    def bounding_box(self):
        box = (self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius )
        return box

    def some_inside(self, maxx, maxy):
        return 0 < self.x + self.radius and self.x - self.radius < maxx and 0 < self.y + self.radius and self.y - self.radius < maxy

    #For checking collisions with walls
    def check_and_reverse(self, maxx, maxy):
        if self.x <= 0: 
            self.vx = self.vx * -1
            self.x = abs(self.x)
            
        if self.x >= maxx:
            self.vx = self.vx * -1
            self.x = 2 * maxx - self.x
            
        if self.y <= 0:
            self.vy = self.vy * -1
            self.y = abs(self.y)
            
        if self.y >= maxy:
            self.vy = self.vy * -1
            self.y = 2 * maxy - self.y

    def velocity(self):
        return (self.vx, self.vy)

    def area(self):
        return (self.radius ** 2) * math.pi

    def rad(self):
        return self.radius
