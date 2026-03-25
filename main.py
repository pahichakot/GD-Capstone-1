#Make it fly
import pgzrun, random

#Setup
WIDTH = 400
HEIGHT = 400

#List of bird positions
next_bird_position = [(200,200), (350, 100), (150, 150)]

#Get actors
bird = Actor("bird")
bird.pos = 200, 200

#Functions
def draw():
    screen.blit("trees",(0,0))
    bird.draw()
    screen.draw.text("Tweet Tweet! ", midtop = (WIDTH/2, 10), fontsize = 30, color = "black")

#Randomly giving bird a target
def next_bird_target():
    x = random.randint(100,300)
    y = random.randint(100, 300)
    bird.target = x,y
    target_angle = bird.angle_to(bird.target)
    target_angle += 360 * ((bird.angle - target_angle + 180) // 360)
    animate(bird, angle = target_angle, duration = 0.3, on_finished = move_bird)

#Moving bird
def move_bird():
    animate(bird, tween = "accel_decel", pos = bird.target, duration = bird.distance_to(bird.target) / 200, on_finished = next_bird_target)

#Calling the function
next_bird_target()
pgzrun.go()