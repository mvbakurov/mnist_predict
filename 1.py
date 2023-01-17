import pandas as pd

df = pd.read_csv('data/mnist_test.csv', header=None)
step=0



import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (280, 280)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    test = df.iloc[step]
    pygame.display.set_caption(str(test[0]))
    test = test[1:]
    step += 1
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    blockSize = 10  # Set the size of the grid block
    i = 0
    for x in range(0, 280, 10):
        for y in range(0, 280, 10):
            color = (test[i], test[i], test[i])
            rect = pygame.Rect(y, x, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect,5)
            i += 1
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    print(test)
    clock.tick(1)

# Close the window and quit.
pygame.quit()
