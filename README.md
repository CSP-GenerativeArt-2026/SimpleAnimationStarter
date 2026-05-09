# SimpleAnimationStarter
Starter code for simple animations made with Tkinter canvas. 

This repository contains two Python code files:
simple_animation.py 
my_animation.py

# simple_animation.py
This is intended to function as a library or drawing API; it contains functions for drawing basic shapes, 
adjusting the state of the canvas tools (such as setting fill color, line thinkness, etc),
and helper functions for determining coordinates for different types of motion. 

## Examples of functions that adjust drawing state:
Call these before using the drawing functions.

```python
def set_fill_color(color_name):
    """Sets the inside color for shapes drawn after this point."""
    global _fill_color
    _fill_color = color_name

def set_outline_color(color_name):
    """Sets the border color for shapes drawn after this point."""
    global _outline_color
    _outline_color = color_name

def set_line_thickness(thickness):
    """Sets the thickness of lines and shape borders."""
    global _line_thickness
    _line_thickness = thickness
```

## Example drawing functions
Call these with appropriate arguments. If you call this with an x or y coordinate that changes
inside the draw_frame() function (see below) you can create moving objects. 

```python
def fill_circle(center_x, center_y, radius):
    """Draws a solid circle given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_circle(center_x, center_y, radius):
    """Draws an empty circle outline given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill="", outline=_outline_color, width=_line_thickness)
```

## Example coordinate functions for movement (based on frame number)
These are used so you don't need to use framenumber directly to calculate positions 
of moving objects. Just pick one for the type of motion you want, call with 
appropriate arguments (including frame_number from draw_frame function) and use the
returned value in your code. See example below in next section. 

```python
def loop_motion(start_val, end_val, speed, frame_number):
    """
    Moves a value from start_val to end_val at the given speed.
    When it reaches end_val, it instantly teleports back to start_val.
    """
    ...

def loop_frames(start_val, end_val, total_frames, frame_number):
    """
    Moves from start_val to end_val taking exactly 'total_frames' to complete.
    Once total_frames is reached, it restarts at start_val.
    """
    ...

def oscillate_motion(min_val, max_val, speed, frame_number):
    """
    Smoothly bounces a value back and forth between min_val and max_val.
    """
    ...

def oscillate_frames(min_val, max_val, total_frames, frame_number):
    """
    Bounces smoothly between min_val and max_val. 
    One full round trip (min -> max -> min) takes exactly 'total_frames'.
    """
    ...

```

Usage:  users should import this module into a separate script, such as my_animation.py
then use the functions inside a draw_frame function body. 

# my_animation.py
In this file you'll write the code to draw your scene or animation. All changes should go
inside the draw_frame function, unless you're defining additional funtions to help organize
the code.

Any additional drawing functions or movement functions should instead go into the 
other file: simple_animation.py

```python
import simple_animation as sa

def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    # ==================================
    # Student code goes below this part
    # ==================================
    sa.fill_background("white") # Clear the background for this frame
   
   # Example Animation: A moving circle in x-direction
    # use the loop_motion funtion to figure out x-coordinate: x_ball
    x_ball = sa.loop_motion(0, width, 5.0, frame_number) # x coordinate
    
    sa.set_fill_color("red")

    # draw the ball; note x coordinate is calculated above; y coord is constant
    sa.fill_circle(x_ball, height / 2, 40)
    
    


if __name__ == "__main__":
    # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)
```
