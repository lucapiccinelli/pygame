from pygame.tests.base_test import pygame_quit
from structure.matrix import Matrix
import pygame
import pygame.image
from pygame.locals import *


def load_tile_table(filename, width, height):
    img = pygame.image.load(filename).convert()
    w, h = img.get_size()
    tile_table = []
    for tile_x in range(0, w/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, h/height):
            rect = (tile_x * width, tile_y * height, width, height)
            line.append(img.subsurface(rect))

    return tile_table


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 128, 98

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._display_surf.fill((255, 255, 255))
        self._running = True
        self._tile_table = load_tile_table(r'res\pgame-tiled-tileset.png', 24, 16)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        for x, row in enumerate(self._tile_table):
            for y, tile in enumerate(row):
                self._display_surf.blit(tile, (x * 32, y * 24))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()

    #m = Matrix()
    #surf = m.to_surface()

    #print surf