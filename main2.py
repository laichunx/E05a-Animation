#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

# Import arcade to let us use the library.
import arcade

# Set the screen width, height, title and a general movement speed.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3

# Ball class
class Ball:
    # Constructor of Ball class to set self variables be the variables come in.
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    # draw method to draw the ball with specific position, radius and color assigned in constructor.
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    # update method to set the position of the ball by adding the change of the position.
    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        # left wall
        if self.position_x < self.radius:
            self.position_x = self.radius

        # right wall
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        # top wall
        if self.position_y < self.radius:
            self.position_y = self.radius

        # bottom wall
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

# MyGame class taking the arcade.Window.
class MyGame(arcade.Window):
    # Constructor of MyGame class
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Set the background of the window to ash grey
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball, with auburn color.
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    # on_draw method to draw the in the window
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        # start the render of arcade, if we do not start, we cannot draw.
        arcade.start_render()
        # draw the ball.
        self.ball.draw()

    # update method, Arcade calls this method every tick.
    def update(self, delta_time):
        self.ball.update()

    # on_key_press method to handle pressing left, right, up, down keys.
    # If any of these keys pressed, goes to that direction with plus or minus MOVEMENT_SPEED.
    # Then assign the value to change_x or change_y and update method will update them every tick.
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    # on_key_release to handle releasing a key.
    # If key is a left or right key, set the change_x to 0.
    # If key is a up or down key, set the change_y to 0.
    # we do this because we want to reset the change_x and change_y when we release the key.
    # if we not reseting the change_x and change_y, the adding will never stop.
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

# main method to setup the window and run the program.
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()