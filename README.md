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
