import pygame
import numpy
from PIL import Image



def get_image(image_path):

    """Get a numpy array of an image so that one can access values[x][y]."""

    image = Image.open(image_path, "r")

    width, height = image.size

    pixel_values = list(image.getdata())

    if image.mode == "RGB":

        channels = 3

    elif image.mode == "L":

        channels = 1

    else:

        print("Unknown mode: %s" % image.mode)

        return None

    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))

    return pixel_values


im = get_image("image/level_1.png")

pygame.init()

win = pygame.display.set_mode((750, 750))

pygame.display.set_caption("Игра")

bg = pygame.image.load('image/level_1.png')

clock = pygame.time.Clock()

x = 50

y = 700

speed = 2



def drawWindow():

    win.blit(bg, (0, 0))

    pygame.draw.circle(win, (0, 255, 0), (x, y), 10)

    pygame.display.update()

run = True


while run:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:# and not(numpy.all(im[x-12][y] == [0, 0, 0])):

        x -= speed

    if keys[pygame.K_RIGHT]:# and not(numpy.all(im[x+12][y] == [0, 0, 0])):

        x += speed

    if keys[pygame.K_UP]:# and not(numpy.all(im[x][y-12] == [0, 0, 0])):

        y -= speed

    if keys[pygame.K_DOWN]:# and not(numpy.all(im[x][y+12] == [0, 0, 0])):

        y += speed

    if y < 100 and x < 140:

        run = False

    drawWindow()

pygame.quit()
