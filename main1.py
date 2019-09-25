#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

# Import arcade to let us create animation
import arcade

# Set the screen width, height and title.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"

# Ball class
class Ball:
    # Constructor of Ball class
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    # draw method to draw the ball
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

# MyGame Class
class MyGame(arcade.Window):

    # Constructor
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # set the background color of the window to ash grey.
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    # on_draw method to draw stuff in the window
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        # start the render of arcade, if we do not start, we cannot draw.
        arcade.start_render()
        # draw the ball.
        self.ball.draw()

    # on_mouse_motion method to handle mouse move, to update the location of the ball to the mouse position
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    # on_mouse_press method to handle mouse press.
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # print a statement of which button you clicked 
        print(f"You clicked button number: {button}")

        # if the button is a left click, set the color of the ball to BLACK.
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK

    # on_mouse_release method to handle mouse press release.
    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        # if the button released is a left mouse button, set the color of the ball to AUBURN.
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN

# main method to setup the window and run the program.
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()