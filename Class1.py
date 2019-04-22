import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MY_BEST_COLOR = (255, 136, 180)

class Rectangle(object):
    def __init__(self, x_pos=0, y_pos=0, change_x=0, change_y=0):
        import random
        self.one = random.randint(0, 255)
        self.two = random.randint(0, 255)
        self.three = random.randint(0, 255)
        self.x_pos1 = random.randint(0, 1400)
        self.y_pos1 = random.randint(0, 900)
        self.height1 = random.randint(20, 70)
        self.width1 = random.randint(20, 70)
        self.change_x1 = random.randint(-3, 3)
        self.change_y1 = random.randint(-3, 3)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.change_x = change_x
        self.change_y = change_y

    def draw(self, height=10, width=10):
        self.height = height
        self.width = width
        pygame.draw.rect(screen, GREEN, (self.x_pos, self.y_pos, self.height, self.width))

    def draw1(self):
        pygame.draw.rect(screen, [self.one, self.two, self.three], (self.x_pos1, self.y_pos1, self.height1, self.width1))

    def randoming(self):
        self.x_pos1 += self.change_x1
        self.y_pos1 += self.change_y1
        if self.x_pos1 > 1400 - self.height1 or self.x_pos1 < 0:
            self.change_x1 *= -1
        elif self.y_pos1 > 900 - self.width1 or self.y_pos1 < 0:
            self.change_y1 *= -1

    def move(self):
        """
        sometimes goes through the edge
        """
        self.x_pos += self.change_x
        self.y_pos += self.change_y
        if self.x_pos > 1400 - self.width or self.x_pos == 0:
            self.change_x *= -1
        elif self.y_pos > 900 - self.height or self.y_pos == 0:
            self.change_y *= -1

# class Randoming(Rectangle):
#     def __init__(self):
#         import random
#         self.x_pos1 = random.randint(0, 1400)
#         self.y_pos1 = random.randint(0, 900)
#         self.height1 = random.randint(20, 70)
#         self.width1 = random.randint(20, 70)
#         self.change_x1 = random.randint(-3, 3)
#         self.change_y1 = random.randint(-3, 3)
#
#     def draw(self):
#         pygame.draw.rect(screen, BLACK, (self.x_pos1, self.y_pos1, self.height1, self.width1))
#
#     def randoming(self):
#         self.x_pos1 += self.change_x1
#         self.y_pos1 += self.change_y1
#         if self.x_pos1 > 1400 - self.height1 or self.x_pos1 < 0:
#             self.change_x1 *= -1
#         elif self.y_pos1 > 900 - self.width1 or self.y_pos1 < 0:
#             self.change_y1 *= -1

class Elipse(Rectangle):
    def draw1(self):
        pygame.draw.ellipse(screen, [self.one, self.two, self.three], (self.x_pos1, self.y_pos1, self.height1, self.width1))

pygame.init()

size = (1400, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("What this")

done = False

my_list = []
for i in range(500):
    my_list.append(Rectangle())
for i in range(500):
    my_list.append(Elipse())

clock = pygame.time.Clock()
my_object = Rectangle(0, 0, 2, 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(MY_BEST_COLOR)

    my_object.draw(50, 50)
    my_object.move()

    for i in my_list:
        i.draw1()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
