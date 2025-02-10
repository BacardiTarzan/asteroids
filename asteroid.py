from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x, y, radius)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            newVec1 = self.velocity.rotate(random_angle)
            newVec2 = self.velocity.rotate(-random_angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            Asteroid1.velocity = newVec1 * 1.2
            Asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            Asteroid2.velocity = newVec2 * 1.2