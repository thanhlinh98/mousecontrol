y_strength = 0
x_strength = 0
g = 5

def on_forever():
    global x_strength, y_strength, g
    mouse.start_mouse_service()
    keyboard.start_keyboard_service()
    x_strength = input.acceleration(Dimension.X)
    y_strength = input.acceleration(Dimension.Y)
    g = 10
    if x_strength > 400 and x_strength < 500:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        mouse.movexy(g, 0)
    if x_strength > 500 and x_strength < 600:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        mouse.movexy(g * 2, 0)
    if x_strength > 600 and x_strength < 700:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        mouse.movexy(g * 3, 0)
    if x_strength > 700 and x_strength < 800:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        mouse.movexy(g * 4, 0)
    if x_strength > 800:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        mouse.movexy(g * 5, 0)
    if x_strength < -400 and x_strength > -500:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        mouse.movexy(0 - g, 0)
    if x_strength < -500 and x_strength > -600:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        mouse.movexy(0 - g * 2, 0)
    if x_strength < -600 and x_strength > -700:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        mouse.movexy(0 - g * 3, 0)
    if x_strength < -700 and x_strength > -800:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        mouse.movexy(0 - g * 4, 0)
    if x_strength < -800:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        mouse.movexy(0 - g * 5, 0)
    if y_strength > 400 and y_strength < 500:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        mouse.movexy(0, g)
    if y_strength > 500 and y_strength < 600:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        mouse.movexy(0, g * 2)
    if y_strength > 600 and y_strength < 700:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        mouse.movexy(0, g * 3)
    if y_strength > 700 and y_strength < 800:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        mouse.movexy(0, g * 4)
    if y_strength > 800:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        mouse.movexy(0, g * 5)
    if y_strength < -400 and y_strength > -500:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        mouse.movexy(0, 0 - g)
    if y_strength < -500 and y_strength > -600:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        mouse.movexy(0, 0 - g * 2)
    if y_strength < -600 and y_strength > -700:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        mouse.movexy(0, 0 - g * 3)
    if y_strength < -700 and y_strength > -800:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        mouse.movexy(0, 0 - g * 4)
    if y_strength < -800:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        mouse.movexy(0, 0 - g * 5)
    if input.button_is_pressed(Button.A):
        mouse.click()
    if input.button_is_pressed(Button.B):
        mouse.right_click()
    if input.button_is_pressed(Button.AB):
        keyboard.send_string("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    basic.clear_screen()
basic.forever(on_forever)
