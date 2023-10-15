import pgzrun
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700
TITLE = "Car Game"

list_cars = ["car" , "car1" , "car2"]

background_menu = Actor("background" , (500 , 350))
start_button = Actor("button_start" , (500 , 350))
background_game = Actor("background_game" , (500 , 350))
back_button = Actor("button_back" , (100 , 100))
car = Actor(random.choice(list_cars) , (500 , 100))
polic = Actor("car" , (50 , 350))
polic.angle = 90

game = False
angle = False
gameover = False
speed = 5
z = random.randint(1050 , 1300)
score = 0
speed_polic = 5

def update():
    global speed , gameover , x , score , speed_polic

    def x():
        global z
        z = random.randint(1050 , 1300)

    if game:
        
        if keyboard.down:
            car.y += speed
        if keyboard.up and car.y >= 67:
            car.y -= speed

        if car.y >= 750:
            car.y = -50
            score += 1
            speed_polic += 2
            car.image = random.choice(list_cars)

        if angle and car.angle <= 85 and gameover == False:
            car.angle += 5
            if speed != 0:
                speed -= 1

        if angle == False and car.angle >= 5 and gameover == False:
            car.angle -= 5
            speed = 5

        if gameover == False:
            polic.x += speed_polic
        else:
            speed = 0

        if polic.x >= z:
            x()
            polic.x = -50

        if car.colliderect(polic):
            gameover = True

    print(z)

    sounds.mester.play()

def draw():
    global menu

    def menu():
        background_menu.draw()
        start_button.draw()
    menu()

    if game:
        background_game.draw()
        back_button.draw()
        car.draw()
        polic.draw()

        screen.draw.text(f"score : {score}" , fontsize = 50 , topleft = (800 , 50) , color = "black")

def on_mouse_down(pos):
    global game , gameover , speed , score

    if start_button.collidepoint(pos):
        game = True
        gameover = False
        speed = 5
        car.angle = 0
        car.y = 100
        polic.x = 50
        score = 0

    if back_button.collidepoint(pos):
        game = False
        menu()

def on_key_down(key):
    global angle

    if key == keys.RIGHT and car.angle <= 5:
        angle = True

    if key == keys.LEFT and car.angle >= 85:
        angle = False

pgzrun.go()