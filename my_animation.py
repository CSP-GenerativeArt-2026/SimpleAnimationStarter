import simple_animation as sa

def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    
    # 1. Clear the background for this frame
    sa.fill_background("white")
    
    # 2. Draw the information text
    sa.set_fill_color("black")
    sa.draw_text(40, 50, f"Frame number: {frame_number}")
    sa.draw_text(40, 80, f"Elapsed Time: {elapsed_seconds:.1f} seconds")
                       
    # 3. Example Animation: A moving circle
    # Using modulo (%) makes the X coordinate wrap around when it hits the width
    # moving_x = (frame_number * 5) % width
    x_ball = sa.loop_motion(0, width, 5.0, frame_number)
    
    sa.set_fill_color("red")
    
    # 4. Example Animation: A moving fish
    repeat_fish = 300 # number of frames to repeat
    x_fish = sa.oscillate_frames(0, width-50, repeat_fish, frame_number)
    y_fish = sa.oscillate_motion(height//2, height//2 +100, 0.15, frame_number)
    sa.fill_circle(x_ball, height // 2, 40)
    if (frame_number % repeat_fish)  < (repeat_fish // 2):
        sa.draw_fish(x_fish, y_fish, 50, "orange", "right")
    else:
        sa.draw_fish(x_fish, y_fish, 50, "orange", "left")
    
    


if __name__ == "__main__":
    # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)
    