"""Module with the canvas class. This is where the animation will
happen"""
from tkinter import *
from math import sin, cos

class ProjectileMotionAnimation(Canvas):

    def __init__(self):
        super().__init__(
            width=1, height=1, highlightthickness=0, bg='skyblue')

        self.floor_height = None
        self.ball = None

        # Variables during animation
        self.h_vel = None
        self.v_vel = None
        self.time = None
        self.total_time = None
        self.time_step = None
        self.no_of_frames = None
        self.total_no_of_frames = None

    def setup_canvas(self):
        """Draw all needed components for the projectile motion 
        animation"""
        self.draw_floor()
        self.draw_ball()
    
    def draw_floor(self):
        """Draw floor of the projectile motion animation"""
        w, h = self.winfo_width(), self.winfo_height()
        # Set floor height
        self.floor_height = h - 10
        self.create_rectangle(0, self.floor_height, w, h, fill='sienna3', outline='sienna3')

    def draw_ball(self):
        """Draw ball on top of the floor"""
        diameter = 50
        offset = 10
        # The -1 is added to raise it one pixel up from the floor so
        # that it lies flat on top of the floor, or else it would
        # dig into the floor one pixel
        self.ball = self.create_oval(
            offset, self.floor_height-diameter-1,
            offset+diameter, self.floor_height-1, fill='red')

    def start_animation(self, init_vel, angle):
        """Starts the animation"""
        self.h_vel = init_vel * cos(angle)
        self.v_vel = init_vel * sin(angle)
        self.g = 9.8
        self.total_time = self.v_vel / ((1/2)*self.g)

        self.no_of_frames = 0
        self.total_no_of_frames = round(self.total_time * 20)
        self.time_step = self.total_time / self.total_no_of_frames
        self.time = self.time_step

        self.starting_ball_coords = self.coords(self.ball)
        self.do_animation()

    def do_animation(self):
        """Completes one frame of the animation and calls for the next one"""
        if self.no_of_frames == self.total_no_of_frames:
            self.reset_animation_vars()
            return  

        # x and y displacement
        x_disp = (self.h_vel * self.time) * 5
        y_disp = ((self.v_vel*self.time) + ((1/2)*-self.g*(self.time**2))) * 5

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
        self.h_vel = None
        self.v_vel = None
        self.time = None
        self.total_time = None
        self.time_step = None
        self.no_of_frames = None
        self.total_no_of_frames = None
