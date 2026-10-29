import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

#Class for asteroid objects
class Asteroid(CircleShape):

    #init function for Asteroid class
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    #overriding draw function from parent
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    #overriding update method. Should go in straight line at constant speed
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
