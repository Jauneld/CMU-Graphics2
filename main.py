from browser import document, window, alert
import random 

def sketch(p):
    # Setup function for p5.js sketch
    def setup():
        p.createCanvas(1250, 500)
        p.background(0)
        p.rectMode(p.CENTER)

    # Draw function for p5.js sketch
    def draw():
        color_list = ["#22577a", "#38a3a5", "#57cc99", "#80ed99", "#c7f9cc"]
        p.noStroke()
        p.fill(random.choice(color_list))
        p.ellipse(p.mouseX, p.mouseY, 50, 50)

    # Mouse pressed function for p5.js sketch
    def mouse_pressed():
        p.background(0)

    # Key pressed function for p5.js sketch
    def key_pressed():
        if p.key == " ":
            print("LOL :)")

    # Assigning the functions to p5 instance
    p.setup = setup
    p.draw = draw
    p.mousePressed = mouse_pressed
    p.keyPressed = key_pressed

# Creating a new p5 instance
myp5 = window.p5.new(sketch)
