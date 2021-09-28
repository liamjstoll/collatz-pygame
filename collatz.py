import pygame
import sys
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)




def collatz(n):
    if n % 2 == 0: # if even, return n/2
        return int(n / 2)
    else:          # if odd, return 3n + 1
        return int(3 * n + 1)

def getCollatzUntilOne(n):
    ans = [n]   # sequence will go here
    while n != 1:
        ans.append(collatz(n))
        n = collatz(n)
    return ans 


n = int(input("enter a number: "))
arr = getCollatzUntilOne(n)

height_multiplier = SCREEN_HEIGHT / max(arr)
width_multiplier = int(SCREEN_WIDTH / len(arr))

ANIMATION_TIME = 5   # in seconds
if len(arr) > 25:
    ANIMATION_TIME = 10
time_per_animation = ANIMATION_TIME / len(arr)   # in seconds


screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])  # open a window
screen.fill((255, 255, 255))

i = 0      # counter for the loop 
last_X = 0
last_Y = 0


# run until quit
running = True
while running and i < len(arr):

    # if exit button pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


  
    pygame.draw.line(screen, RED, (last_X,SCREEN_HEIGHT - last_Y),(i * width_multiplier, SCREEN_HEIGHT - arr[i] * height_multiplier))
    last_X = i * width_multiplier
    last_Y = arr[i] * height_multiplier
    textsurface = myfont.render(str(arr[i]), False, (0, 0, 0))  
    screen.blit(textsurface,(i * width_multiplier, SCREEN_HEIGHT - arr[i] * height_multiplier))
    i += 1

    print(last_X,last_Y)

    time.sleep(time_per_animation)

    pygame.display.flip()

time.sleep(time_per_animation)

print(len(arr))
print(arr)

pygame.quit()
    
#pygame.draw.circle(screen), BLUE, circle_x_&_y, circle_radius, border_width)

#pygame.draw.line(screen, RED, start_pos, end_pos, width)

