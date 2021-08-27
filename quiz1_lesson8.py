import turtle as t
import random

def get_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

def draw_rectangle(x, y, color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.forward(x)
        else:
            t.forward(y)
        t.left(90)
    t.end_fill()
    t.penup()
    t.home()

if __name__ == '__main__':
    t.pensize(3)
    t.penup()
    t.speed(10)
    t.colormode(255)

    # tỷ lệ bản vẽ
    k = 5

    # Vẽ nhà cao tầng
    x = 50                  # chiều rộng một căn hộ
    y = 50                  # chiều cao một căn hộ
    for i in range(4):
        t.left(90 * i)
        draw_rectangle(k*50, k*50, get_color())
    #print(t.position())

    # Vẽ cửa sổ nhà cao tầng
    list = [(-40, 10), (-40, -40), (10, -40), (10, 10)]
    x1 = 30                 # chiều rộng cửa sổ
    y1 = 30                 # chiều cao cửa sổ

    for i in range(len(list)):
        t.goto(k * list[i][0], k * list[i][1])
        draw_rectangle(k*x1, k*y1, get_color())
    
    # vẽ nhà cấp 4
    t.goto(k * 50, k * -50)
    x2 = 100
    y2 = 50
    draw_rectangle(k * x2, k * y2, get_color())
    
    # vẽ cửa chính nhà cấp 4
    t.goto(k * 70, k * -50)
    x3 = 60
    y3 = 30
    draw_rectangle(k * x3, k * y3, get_color())
    
    t.hideturtle()
    t.done()