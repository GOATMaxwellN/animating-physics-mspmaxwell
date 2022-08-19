"""Module with the canvas class. This is where the animation will
happen"""
from tkinter import *
from math import sin, cos


class ProjectileMotionAnimation(Canvas):

    def __init__(self):
        super().__init__(
            width=1, height=1, highlightthickness=0, bg='skyblue')
        self.bind("<Configure>", self.on_resize)

        # Ball attributes
        self.ball = None
        self.offset = 10
        self.diameter = 50
        # Floor attributes
        self.floor = None
        self.floor_height = None

        # Variables during animation
        self.animation_running = False
        self.h_vel = None
        self.v_vel = None
        self.time = None
        self.total_time = None
        self.time_step = None
        self.no_of_frames = None
        self.total_no_of_frames = None

        self.time_to_total_frames_multiplier = 20
        self.upc = 5  # unit to pixel conversion

    def setup_canvas(self):
        """Draw all needed components for the projectile motion 
        animation"""
        self.draw_floor()
        self.draw_ball()
    
    def draw_floor(self, resize = False):
        """Draw floor of the projectile motion animation"""
        w, h = self.winfo_width(), self.winfo_height()
        # Set floor height
        self.floor_height = h - 10
        if resize:
            self.coords(self.floor, 0, self.floor_height, w, h)
        else:
            self.floor = self.create_rectangle(
                0, self.floor_height, w, h, fill='sienna3', outline='sienna3')

    def draw_ball(self, resize = False):
        """Draw ball on top of the floor"""
        # The -1 is added to raise it one pixel up from the floor so
        # that it lies flat on top of the floor, or else it would
        # dig into the floor one pixel
        if resize:
            cur_ball_coords = self.coords(self.ball)
            # Retain x coordinates. We only change y coordinates upon resize.
            tl_x, br_x = cur_ball_coords[0], cur_ball_coords[2]
            self.coords(
                self.ball,
                tl_x, self.floor_height-self.diameter-1,
                br_x, self.floor_height-1)
        else:
            self.ball = self.create_oval(
                self.offset, self.floor_height-self.diameter-1,
                self.offset+self.diameter, self.floor_height-1, fill='red')

    def reset_ball_position(self):
        """Brings ball back to its default position"""
        self.coords(
                self.ball,
                self.offset, self.floor_height-self.diameter-1,
                self.offset+self.diameter, self.floor_height-1)

    def start_animation(self, init_vel, angle):
        """Starts the animation"""
        self.h_vel = init_vel * cos(angle)
        self.v_vel = init_vel * sin(angle)
        self.g = 9.8
        self.total_time = self.v_vel / ((1/2)*self.g)

        self.no_of_frames = 0
        self.total_no_of_frames = \
            round(self.total_time * self.time_to_total_frames_multiplier)
        self.time_step = self.total_time / self.total_no_of_frames
        self.time = self.time_step

        self.starting_ball_coords = self.coords(self.ball)

        self.animation_running = True
        self.do_animation()

    def do_animation(self):
        """Completes one frame of the animation and calls for the next one"""
        if self.no_of_frames == self.total_no_of_frames:
            self.reset_animation_vars()
            return  

        # x and y displacement
        x_disp = (self.h_vel * self.time) * self.upc
        y_disp = ((self.v_vel*self.time)
                 + ((1/2)*-self.g*(self.time**2))) * self.upc

        # Get the starting coordinates of the ball
        # tl = top left    # br = bottom right
        tl_x, tl_y, br_x, br_y = self.starting_ball_coords

        # New x and y coordinates
        new_tl_x, new_tl_y = round(tl_x + x_disp), round(tl_y - y_disp)
        new_br_x, new_br_y = round(br_x + x_disp), round(br_y - y_disp)

        # Set the new coordinates to the ball
        self.coords(self.ball, new_tl_x, new_tl_y, new_br_x, new_br_y)

        # Increment time and update no_of_frames and schedule next frame
        self.no_of_frames += 1
        self.time += self.time_step
        self.after(1000//30, self.do_animation)

    def reset_animation_vars(self):
        self.animation_running = False
        self.h_vel = None
        self.v_vel = None
        self.time = None
        self.total_time = None
        self.time_step = None
        self.no_of_frames = None
        self.total_no_of_frames = None

    def abort_animation(self, msg = ""):
        """Aborts the animation by bringing the ball back down to the
        floor. Happens when the window is resized."""
        self.reset_animation_vars()
        self.reset_ball_position()

        self.show_message(msg)

    def show_message(self, msg):
        """Adds some temporary text to the top left corner of the canvas"""
        text = self.create_text(10, 10, text=msg, anchor=NW)
        self.after(2000, lambda: self.delete(text))

    def on_resize(self, event):
        """Makes sure that the ball and floor are brought up to the
        bottom of the canvas upon resizing."""
        if self.floor is not None:
            self.draw_floor(resize=True)
        if (self.ball is not None):
            self.draw_ball(resize=True)
            if self.animation_running:
                self.abort_animation("Animation aborted due to resize")
