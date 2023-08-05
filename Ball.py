import math

class Ball(object):

    def __init__(self, pos_x, pos_y, dx, dy, r, c, m_ = 1):
        self.x = pos_x
        self.y = pos_y
        self.vx = dx
        self.vy = dy
        self.ax = 0
        self.ay = 0
        self.radius = r
        self.color = c
        self.mass = m_

    def __str__(self):
        return str(self.x)+ ", " + str(self.y) + ' ' + str(self.radius) + self.color

    def position(self):
        return (self.x, self.y)

    def check_intersect(self, b2):
        x1 = self.position()[0]
        y1 = self.position()[1]
        x2 = b2.position()[0]
        y2 = b2.position()[1]
        dist = math.sqrt((y2 - y1)**2 + (x2 - x1)**2 )
        r1 = abs(self.rad())
        r2 = abs(b2.rad())
        return dist <= r1 + r2

    def distance(self, b2):
        x_dist = abs(self.x - b2.x)
        y_dist = abs(self.y - b2.y)
        return math.sqrt(x_dist**2 + y_dist**2)

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

    def speed(self):
        return math.sqrt(self.vx**2 + self.vy**2)

    def area(self):
        return (self.radius ** 2) * math.pi

    def rad(self):
        return self.radius
