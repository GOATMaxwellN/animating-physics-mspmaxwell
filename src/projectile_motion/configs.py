"""Module that holds the params for projectile motion"""
from tkinter import *
from tkinter import ttk
from math import radians

class ProjectileMotionConfigs(ttk.Frame):

    def __init__(self):
        super().__init__(width=1, height=1)
        # ttk.Style(self).configure('TFrame', background='pink')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        
        # Add entry widgets to collect projectile motion info
        self.setup_configs()

    def setup_configs(self):
        """Add the entry widgets to collect information"""
        # Widget to get initial velocity
        self.init_velocity = IntVar()
        ttk.Label(self, text='Initial Velocity').grid(row=0, column=0, sticky='S')
        ttk.Spinbox(self, from_=0, to=9999,
                    textvariable=self.init_velocity).grid(row=1, column=0,
                                                         sticky='N')

        # Widget to get angle
        self.angle = IntVar()
        ttk.Label(self, text='Angle').grid(row=0, column=1, sticky='S')
        ttk.Spinbox(self, from_=0, to=90,
                    textvariable=self.angle).grid(row=1,column=1, sticky='N')

        # Button to start animation
        self.start_animation_btn = ttk.Button(self, text='Start Animation')
        self.start_animation_btn.grid(row=0, column=2)

    def set_button_command(self, do_animation):
        """Set the 'Start Animation' button command to the function
        that starts the animation"""
        self.start_animation_btn.configure(command=do_animation)

    def get_init_velocity(self):
        return self.init_velocity.get()

    def get_angle(self):
        return radians(self.angle.get())

    