import pgzrun
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700
TITLE = "Car Game"

background_menu = Actor("background" , (500 , 350))
start_button = Actor("button_start" , (500 , 350))
background_game = Actor("background_game" , (500 , 350))
back_button = Actor("button_back" , (100 , 100))
car = Actor("car" , (500 , 100))
polic = Actor("car" , (50 , 350))
polic.angle = 90

game = False
angle = False
gameover = False
speed = 5

def update():
    global speed , gameover

    if game:
        
        if keyboard.down:
            car.y += speed
        if keyboard.up and car.y >= 67:
            car.y -= speed

        if car.y >= 750:
            car.y = -50

        if angle and car.angle <= 85 and gameover == False:
            car.angle += 5
            if speed != 0:
                speed -= 1

        if angle == False and car.angle >= 5 and gameover == False:
            car.angle -= 5
            speed = 5

        if gameover == False:
            polic.x += 5
        else:
            speed = 0

        if polic.x >= 1050:
            polic.x = -50

        if car.colliderect(polic):
            gameover = True

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

def on_mouse_down(pos):
    global game , gameover , speed

    if start_button.collidepoint(pos):
        game = True
        gameover = False
        speed = 5
        car.angle = 0
        car.y = 100
        polic.x = 50

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