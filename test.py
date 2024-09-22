import pygame

pygame.init()

screen_w = 1000
screen_h = 800

screen = pygame.display.set_mode((screen_w, screen_h))

fps = 60
timer = pygame.time.Clock()

wall_thickness = 10
gravity = 0.5
bounce_stop = 0.3


class ball:
    def __init__(self, x_pos, y_pos, radius, colour, mass, retention, y_speed, x_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.colour = colour
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ''
        self.selected = False

    
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.colour,(self.x_pos, self.y_pos), self.radius)
    
    def check_gravity(self):
        if self.y_pos < screen_h - self.radius - (wall_thickness/2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed *-1 *self.retention
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
        return self.y_speed
    
    def update_pos(self, mouse):
        
        if not self.selected:
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed

        else:
             self.x_pos += mouse[0]
             self.y_pos += mouse[1]
    
    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected




def draw_walls():
    left = pygame.draw.line(screen, 'white', (0,0), (0,screen_h),wall_thickness)
    right = pygame.draw.line(screen, 'white', (screen_w,0), (screen_w,screen_h),wall_thickness)
    top = pygame.draw.line(screen, 'white', (0,0), (screen_w,0),wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0,screen_h), (screen_w,screen_h),wall_thickness)
    wall_list=[left, right, top, bottom]
    return wall_list



ball1 = ball(50, 50, 30, (0,0,255), 100, .65, 0, 0, 1)
ball2 = ball(500, 75, 50, (0,255,0), 100, .8, 0, 0, 2)
ball3 = ball(750, 60 ,40,(255, 0, 0), 100, .85, 0, 0, 3)
balls = [ball1, ball2]



run = True
while run:
    timer.tick(fps)

    screen.fill((0,0,0))

    mouse_pos = pygame.mouse.get_pos()

    walls = draw_walls()
    ball1.draw()
    ball2.draw()
    ball3.draw()

    ball1.update_pos(mouse_pos)
    ball2.update_pos(mouse_pos)
    ball3.update_pos(mouse_pos)


    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed = ball2.check_gravity()
    ball3.y_speed = ball3.check_gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ball1.check_select(event.pos) or ball2.check_select(event.pos):
                    active_select = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                for i in range(len(balls)):
                    balls[i].check_select((-1000, -1000))

    pygame.display.flip()

pygame.quit()
