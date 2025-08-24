import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption("Mountain Shooter")
print("Setup end")

print("Loop start")
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() # Close window
      quit() # end pygame