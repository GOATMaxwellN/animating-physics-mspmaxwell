# Projectile Motion Animation
A configurable projectile motion animation made with tkinter.

## How to use
![Image of the Projectile Motion Animation GUI][image-of-gui]

The bottom of the GUI contains the animation configurations. You can increase or decrease the value for initial velocity and angle, after which you click 'Start Animation' and watch the ball go.

> For the physics inclined, this animation assumes no force in the horizontal direction, and only the force of gravity on the vertical direction. Hopefully this will change in the future when I expand on this.

## How to setup
Make sure you have Python 3.5+ installed

Clone this repo and `cd` into it

Run `py src/projectile_motion_animation/main.py` on the terminal.

## Goals
Short term:
- ~Make application resizable (to some minimum size)~ DONE
- Allow user to change initial height of ball
- Add axis scales that allow user to see at a glance how far the ball has gone

Long term (because I have to learn more physics):
- Allow ball to bounce

[image-of-gui]: https://github.com/GOATMaxwellN/projectile-motion-animation/blob/main/README_IMAGES/projectile_motion_animation_gui.png "Image of how the application looks like"
