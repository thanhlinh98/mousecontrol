let y_strength = 0
let x_strength = 0
let g = 5
basic.forever(function on_forever() {
    
    mouse.startMouseService()
    x_strength = input.acceleration(Dimension.X)
    y_strength = input.acceleration(Dimension.Y)
    g = 10
    if (x_strength > 400 && x_strength < 500) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        `)
        mouse.movexy(g, 0)
    }
    
    if (x_strength > 500 && x_strength < 600) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        `)
        mouse.movexy(g * 2, 0)
    }
    
    if (x_strength > 600 && x_strength < 700) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        `)
        mouse.movexy(g * 3, 0)
    }
    
    if (x_strength > 700 && x_strength < 800) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        `)
        mouse.movexy(g * 4, 0)
    }
    
    if (x_strength > 800) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        `)
        mouse.movexy(g * 5, 0)
    }
    
    if (x_strength < -400 && x_strength > -500) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        `)
        mouse.movexy(0 - g, 0)
    }
    
    if (x_strength < -500 && x_strength > -600) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        `)
        mouse.movexy(0 - g * 2, 0)
    }
    
    if (x_strength < -600 && x_strength > -700) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        `)
        mouse.movexy(0 - g * 3, 0)
    }
    
    if (x_strength < -700 && x_strength > -800) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        `)
        mouse.movexy(0 - g * 4, 0)
    }
    
    if (x_strength < -800) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        `)
        mouse.movexy(0 - g * 5, 0)
    }
    
    if (y_strength > 400 && y_strength < 500) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        `)
        mouse.movexy(0, g)
    }
    
    if (y_strength > 500 && y_strength < 600) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        `)
        mouse.movexy(0, g * 2)
    }
    
    if (y_strength > 600 && y_strength < 700) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        `)
        mouse.movexy(0, g * 3)
    }
    
    if (y_strength > 700 && y_strength < 800) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        `)
        mouse.movexy(0, g * 4)
    }
    
    if (y_strength > 800) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        `)
        mouse.movexy(0, g * 5)
    }
    
    if (y_strength < -400 && y_strength > -500) {
        basic.showLeds(`
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        `)
        mouse.movexy(0, 0 - g)
    }
    
    if (y_strength < -500 && y_strength > -600) {
        basic.showLeds(`
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        `)
        mouse.movexy(0, 0 - g * 2)
    }
    
    if (y_strength < -600 && y_strength > -700) {
        basic.showLeds(`
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        `)
        mouse.movexy(0, 0 - g * 3)
    }
    
    if (y_strength < -700 && y_strength > -800) {
        basic.showLeds(`
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        `)
        mouse.movexy(0, 0 - g * 4)
    }
    
    if (y_strength < -800) {
        basic.showLeds(`
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        `)
        mouse.movexy(0, 0 - g * 5)
    }
    
    if (input.buttonIsPressed(Button.A)) {
        mouse.click()
    }
    
    if (input.buttonIsPressed(Button.B)) {
        mouse.rightClick()
    }
    
    basic.clearScreen()
})
