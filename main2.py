#Ship must touch the balloon. Once score is 15 points, game ends.
import pgzrun, random

#Set up
HEIGHT = 800
WIDTH = 800

#Get actors
ship = Actor("spaceship")
ship.pos= 50,50

asteroid = Actor("asteroid")

x = random.randint(50, 750)
y = random.randint(50, 750)
asteroid.pos = x, y

balloon = Actor("balloon")

x = random.randint(50, 750)
y = random.randint(50, 750)
balloon.pos = x,y

#Get variables
score = 0
game_over = False

#Draw
def draw():
    screen.clear()
    ship.draw()
    balloon.draw()
    asteroid.draw()
    screen.draw.text("Score : "+str(score), (20,20), fontsize = 30, color = "white")

    if game_over:
        screen.draw.text("Game Over ! You won !", (400, 400), fontsize = 50, color = "white")

#Moving balloon
def move_balloon():
    balloon.x = random.randint(50, 700)
    balloon.y = random.randint(50, 700)

#Moving asteroid
def move_asteroid():
    balloon.x = random.randint(50, 750)
    balloon.y = random.randint(50, 750)

#Code ship to move based on arrow keys
def update():
    global score, game_over
    if keyboard.left:
        ship.x = ship.x - 2
    if keyboard.right:
        ship.x = ship.x + 2
    if keyboard.up:
        ship.y = ship.y - 2
    if keyboard.down:
        ship.y = ship.y + 2
    
    if ship.colliderect(balloon):
        score = score + 1
        move_balloon()
        move_asteroid()
    if ship.colliderect(asteroid):
        score = score - 1
        move_balloon()
        move_asteroid()

    if score == 15:
        game_over = True

pgzrun.go()