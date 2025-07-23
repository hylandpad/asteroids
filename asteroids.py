from circleshape import CircleShape
import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vectors = [self.velocity.rotate(random_angle),self.velocity.rotate(-random_angle)]
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            for vector in vectors:
                asteroid = Asteroid(self.position.x,self.position.y,new_radius)
                asteroid.velocity = vector * 1.2

