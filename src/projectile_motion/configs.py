"""Module that holds the params for projectile motion"""
from tkinter import *
from tkinter import ttk
from math import radians
from typing import Callable

from animation import ProjectileMotionAnimation

class ProjectileMotionConfigs(ttk.Frame):
    """Holds interface to modify the animation.

    This Frame widget holds the widgets and buttons that allow
    the user to modify the animation as they wish.

    animation : ProjectileMotionAnimation
        Canvas widget that handles drawing the animation.
    init_velocity : IntVar
        Holds what user enters as their initial velocity of choice.
    angle : IntVar
        Holds what user enters as their angle of choice.
    start_animation_btn : ttk.Button
        Button that allows user to start the animation.
    reset_ball_btn : ttk.Button
        Button that allows user to bring the ball back to its default
        position. 
    """

    def __init__(self, animation: ProjectileMotionAnimation):
        super().__init__(width=1, height=1)
        self.animation = animation

        self.init_velocity = IntVar()
        self.angle = IntVar()
        self.start_animation_btn = None  # Created in setup_configs()
        self.reset_ball_btn = None

        # ttk.Style(self).configure('TFrame', background='pink')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        
        # Add entry widgets to collect projectile motion info
        self.setup_configs()

    def setup_configs(self) -> None:
        """Add the entry widgets to collect information"""
        # Widget to get initial velocity
        ttk.Label(self, text='Initial Velocity').grid(row=0, column=0, sticky='S')
        ttk.Spinbox(self, from_=0, to=9999,
                    textvariable=self.init_velocity).grid(row=1, column=0,
                                                         sticky='N')

        # Widget to get angle
        ttk.Label(self, text='Angle').grid(row=0, column=1, sticky='S')
        ttk.Spinbox(self, from_=0, to=90,
                    textvariable=self.angle).grid(row=1,column=1, sticky='N')

        # Add the 'start', 'reset', and 'abort' buttons
        self.create_buttons_frame()

    def create_buttons_frame(self) -> None:
        """Creates a Frame which holds the three main buttons.
        
        Creates a Frame with its own grid, adds it the configs frame,
        and places the 'start', 'reset', and 'abort' buttons in it"""

        def add_button(text: str,
                       command: Callable[[], None]) -> ttk.Button:
            """Adds a button to the buttons_frame.
            
            text : str
                Text shown on the button.
            command : func
                Function called when button is clicked."""
            btn = ttk.Button(buttons_frame, text=text, command=command)
            btn.pack(side=TOP, pady=(2,0), ipadx=5, ipady=2)
            return btn

        # Create the frame, add it to the Configs frame and set up
        # its grid.
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=0, column=2, rowspan=2)
        for i in range(3):
            buttons_frame.rowconfigure(i, weight=1)
        buttons_frame.columnconfigure(0, weight=1)
        
        # Add the three buttons to the frame
        # Button to start animation
        self.start_animation_btn = add_button(
            "Start Animation", self.start_animation)

        # Button to reset ball position (place ball back into default position)
        self.reset_ball_btn = add_button(
            "Reset Animation", self.reset_ball_position)

        # Button to abort a running animation    
        self.abort_animation_btn = add_button(
            "Abort Animation", self.abort_animation)        

    def get_init_velocity(self) -> int:
        return self.init_velocity.get()

    def get_angle(self) -> int:
        return radians(self.angle.get())

    def start_animation(self) -> None:
        init_vel = self.get_init_velocity()
        angle = self.get_angle()
        self.animation.start_animation(init_vel, angle)

        # Disable the reset ball button and start animation button
        self.reset_ball_btn.configure(state=DISABLED)
        self.start_animation_btn.configure(state=DISABLED)
        # Periodically check if the animation is still running so as
        # to re-enable the two buttons.
        self.checkIfAnimationRunning() 

    def reset_ball_position(self) -> None:
        self.animation.reset_ball_position()

    def abort_animation(self) -> None:
        ...

    def checkIfAnimationRunning(self) -> None:
        # If animation is still running, check again a bit later
        if self.animation.animation_running:
            self.after(500, self.checkIfAnimationRunning)
        else:
            # Re-enable the 'reset ball' and 'start animation' button
            self.reset_ball_btn.configure(state=ACTIVE)
            self.start_animation_btn.configure(state=ACTIVE)
