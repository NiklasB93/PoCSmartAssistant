
from image_pp import ImageManager
from PIL import Image
from eye_tracking_interface import EyeTrackingInterface

from threading import Thread
import time

from gui import GUI


class POCMaster:
    running = True
    gui = GUI()
    eye_tracking = EyeTrackingInterface()


    def __init__(self):
        # image_manager = ImageManager()

        self.eye_tracking.start_server()

        mainLoop = Thread(target=self.main_loop)
        self.running = True
        mainLoop.start()

        self.gui.start()


        self.running = False
        mainLoop.join()


    def main_loop(self):
        while self.running:
            time.sleep(2)

            self.gui.change_image(1)




