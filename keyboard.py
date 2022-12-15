x_strength = 0
y_strength = 0
turn_left = ""
turn_right = ""

def on_forever():
    global x_strength, y_strength, turn_left, turn_right
    keyboard.start_keyboard_service()
    x_strength = input.acceleration(Dimension.X)
    y_strength = input.acceleration(Dimension.Y)
    turn_left = "aaaaaaaaaa"
    turn_right = "dddddddddd"
    if x_strength > 400 and x_strength < 500:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string(turn_right)
    if x_strength > 500 and x_strength < 600:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string("dddddddddddddddddddd")
    if x_strength > 600 and x_strength < 700:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string("dddddddddddddddddddddddddddddd")
    if x_strength > 700 and x_strength < 800:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string("dddddddddddddddddddddddddddddddddddddddd")
    if x_strength > 800 and x_strength < 900:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string("dddddddddddddddddddddddddddddddddddddddddddddddddd")
    if x_strength > 900:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        keyboard.send_string("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    if x_strength < -400 and x_strength > -500:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string(turn_left)
    if x_strength < -500 and x_strength > -600:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaa")
    if x_strength < -600 and x_strength > -700:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if x_strength < -700 and x_strength > -800:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if x_strength < -800 and x_strength > -900:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if x_strength < -800 and x_strength > -900:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if x_strength < -800 and x_strength > -900:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if x_strength < -900:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        keyboard.send_string("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        keyboard.send_string("ssssssssssssss")
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        keyboard.send_string("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    basic.clear_screen()
basic.forever(on_forever)
