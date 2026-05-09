import math
import tkinter as tk
import time

# Internal state variables to track the "paintbrush"
_canvas = None
_fill_color = "black"
_outline_color = "black"
_line_thickness = 1

def start(draw_frame_function, width=800, height=600):
    """Sets up the animation loop and calls the student's function every frame."""
    global _canvas
    
    root = tk.Tk()
    root.title("Simple Animation")
    root.resizable(False, False)
    
    _canvas = tk.Canvas(root, width=width, height=height, bg="white", highlightthickness=0)
    _canvas.pack()
    
    # State variables for the animation
    start_time = time.time()
    frame_number = 0
    
    def animate():
        nonlocal frame_number
        
        # Clear the canvas for the new frame
        _canvas.delete("all")
        
        # Calculate elapsed time
        elapsed_seconds = time.time() - start_time
        
        # Call the student's drawing function (Notice we don't pass the canvas anymore)
        draw_frame_function(frame_number, elapsed_seconds, width, height)
        
        frame_number += 1
        
        # Schedule the next frame in ~16 milliseconds (approx 60 FPS)
        root.after(16, animate)

    # Start the animation loop
    animate()
    root.mainloop()
    
    
# =====================================================================
# ANIMATION FUNCTIONS API
# These will calculate coordinates for you for different kinds of motion.
# Use these functions in your code!
# =====================================================================

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



def oscillate_motion(min_val, max_val, speed, frame_number):
    """
    Smoothly bounces a value back and forth between min_val and max_val.
    """
    # Find the exact middle between the two values
    midpoint = (min_val + max_val) / 2
    
    # Find how far it can stretch from the middle (the amplitude)
    amplitude = (max_val - min_val) / 2
    
    # Calculate the sine wave (returns a value between -1 and 1)
    # We scale the speed down slightly so the animation isn't too frantic
    wave = math.sin(frame_number * (speed * 0.05))
    
    # Apply the wave to the amplitude and add it to the midpoint
    return midpoint + (amplitude * wave)



# Here's an alternative function that oscillates based on a fixed number of frames
def oscillate_frames(min_val, max_val, total_frames, frame_number):
    """
    Bounces smoothly between min_val and max_val. 
    One full round trip (min -> max -> min) takes exactly 'total_frames'.
    """
    # Calculate progress through the cycle (0.0 to 1.0)
    progress = (frame_number % total_frames) / total_frames
    
    # Convert that progress to an angle for a wave (0 to 2*PI)
    angle = progress * 2 * math.pi
    
    # -math.cos starts at -1, goes to 1, and back to -1
    wave = -math.cos(angle)
    
    # Calculate the midpoint and amplitude (how far it stretches from the middle)
    midpoint = (min_val + max_val) / 2
    amplitude = (max_val - min_val) / 2
    
    # Apply the wave to the amplitude and midpoint
    return midpoint + (amplitude * wave)


# =====================================================================
# DRAWING API 
# Use these functions in your code!
# You can add new functions here to draw more things
# =====================================================================


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

def fill_background(color_name):
    """Fills the entire canvas with one solid color."""
    w = int(_canvas['width'])
    h = int(_canvas['height'])
    _canvas.create_rectangle(0, 0, w, h, fill=color_name, outline="")

def draw_line(x1, y1, x2, y2):
    """Draws a line connecting point (x1, y1) to point (x2, y2)."""
    _canvas.create_line(x1, y1, x2, y2, fill=_outline_color, width=_line_thickness)

def fill_rectangle(x, y, width, height):
    """Draws a solid rectangle with its top-left corner at (x, y)."""
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_rectangle(x, y, width, height):
    """Draws an empty rectangle outline with its top-left corner at (x, y)."""
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill="", outline=_outline_color, width=_line_thickness)

def fill_circle(center_x, center_y, radius):
    """Draws a solid circle given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_circle(center_x, center_y, radius):
    """Draws an empty circle outline given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill="", outline=_outline_color, width=_line_thickness)

def draw_text(x, y, text_string, font_size=16):
    """Draws text on the screen with the top-left corner at (x, y)."""
    _canvas.create_text(x, y, text=text_string, fill=_fill_color, 
                        anchor="nw", font=("Arial", font_size))
    
def fill_triangle(x1, y1, x2, y2, x3, y3):
    """Draws a solid triangle connecting the three given points."""
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    """Draws an empty triangle outline connecting the three given points."""
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill="", outline=_outline_color, width=_line_thickness)


def draw_fish(x, y, size, color, direction):
    """
    Draws a fish facing either left or right.
    
    AI Attribution: This function was generated using Gemini.
    Original Student Prompt: "Can you update the function with one extra parameter that has the fish direction, 'left' or 'right' and points the fish in that direction"
    """
    if direction == "right":
        # Tail on the left
        tail_points = [
            x, y + size / 2,
            x - size / 4, y + size / 4,
            x - size / 4, y + 3 * size / 4
        ]
        # Eye on the right
        eye_x = x + 3 * size / 4
    else:
        # Tail on the right
        tail_points = [
            x + size, y + size / 2,
            x + size + size / 4, y + size / 4,
            x + size + size / 4, y + 3 * size / 4
        ]
        # Eye on the left
        eye_x = x + size / 4

    # Draw the tail
    _canvas.create_polygon(tail_points, fill=color, outline=_outline_color, width=_line_thickness)
    
    # Draw the body
    _canvas.create_oval(x, y, x + size, y + size, fill=color, outline=_outline_color, width=_line_thickness)
    
    # Draw the eye
    eye_radius = size / 10
    eye_y = y + size / 3
    _canvas.create_oval(eye_x - eye_radius, eye_y - eye_radius, 
                        eye_x + eye_radius, eye_y + eye_radius, 
                        fill="white", outline="black", width=1)
    
