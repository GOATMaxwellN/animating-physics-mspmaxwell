"""Module that holds the main window"""

from animation import ProjectileMotionAnimation
from configs import ProjectileMotionConfigs


class MainWindow:

    def __init__(self, root):
        self.root = root  # root is the Tk instance
        self.animation = ProjectileMotionAnimation()  # canvas that will show the animation
        # provides us with parameters of projectile motion (velocity, angle)
        self.configs = ProjectileMotionConfigs(self.animation)

        # Make fullscreen  (application only works in fullscreen)
        # Resizing screen puts canvas out of wack
        self.root.title("Projectile Motion Animation")
        sc_width, sc_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # self.root.geometry(f"{sc_width}x{sc_height}")
        self.root.state('zoomed')
        self.root.minsize(512, 288)

        # Set grid weight
        self.root.rowconfigure(0, weight=4)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Set canvas and configs
        self.animation.grid(row=0, column=0, sticky='NEWS')
        self.configs.grid(row=1, column=0, sticky='NEWS')

        # Draw components of canvas (must be called after adding to grid)
        self.root.update()
        self.animation.setup_canvas()
