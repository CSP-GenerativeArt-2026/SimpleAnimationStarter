# SimpleAnimationStarter
Starter code for simple animations made with Tkinter canvas. 

This repository contains two Python code files:
simple_animation.py 
my_animation.py

# simple_animation.py
This is intended to function as a library or drawing API; it contains functions for drawing basic shapes, 
adjusting the state of the canvas tools (such as setting fill color, line thinkness, etc),
and helper functions for determining coordinates for different types of motion. 

Examples of functions that adjust drawing state:
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

Example drawing functions
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

Example coordinate mapping functions (based on frame number)
```
def loop_motion(start_val, end_val, speed, frame_number):
    """
    Moves a value from start_val to end_val at the given speed.
    When it reaches end_val, it instantly teleports back to start_val.
    """
    # Calculate the total distance it is allowed to travel
    travel_range = end_val - start_val
    
    # Calculate how far it has moved, wrapping around using modulo
    distance_moved = (frame_number * speed) % travel_range
    
    # Return the new current position
    return start_val + distance_moved

# Here's an alternative function that loops based on a fixed number of frames
def loop_frames(start_val, end_val, total_frames, frame_number):
    """
    Moves from start_val to end_val taking exactly 'total_frames' to complete.
    Once total_frames is reached, it restarts at start_val.
    """
    # Calculate how far along we are in the current cycle (0.0 to 1.0)
    # Using modulo (%) keeps the frame counter wrapping around the total_frames limit
    progress = (frame_number % total_frames) / total_frames
    
    # Calculate the total distance
    total_distance = end_val - start_val
    
    # Return the starting position plus the percentage of distance covered
    return start_val + (total_distance * progress)
```

