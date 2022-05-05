import PIL.ImageOps
from PIL import Image
from PIL.ImageQt import ImageQt

class ImageManager:
    raw_image = Image.Image()
    current_image = Image.Image()
    image_name = "cockpit.jpg"

    screen_height = 800
    screen_width = 500

    def __init__(self):
        self.init_image()
        pass

    def init_image(self):
        self.current_image = Image.open(self.image_name)
        self.current_image = self.changeImageSize(self.current_image)
        self.current_image = self.current_image.convert("RGBA")
        self.raw_image = self.current_image

    def reset_image(self):
        self.current_image = self.raw_image

    def get_image(self):
        return self.current_image

    def get_qt_image(self):
        return ImageQt(self.current_image)

    def add_mask(self, mask_name, alpha_val):
        mask_image = Image.open(mask_name)
        mask_image = self.changeImageSize(mask_image)
        mask_image = mask_image.convert("RGBA")
        # blend current image with mask
        self.current_image = Image.blend(self.current_image, mask_image, alpha=alpha_val)

    # Function to change the image size
    def changeImageSize(self, image):
        widthRatio = self.screen_width / image.size[0]
        heightRatio = self.screen_height / image.size[1]

        newWidth = int(widthRatio * image.size[0])
        newHeight = int(heightRatio * image.size[1])

        newImage = image.resize((newWidth, newHeight))
        return newImage

#
# # Take two images for blending them together
# image1 = Image.open("./cockpit.jpg")
# image2 = Image.open("./red_mask.png")
# image2_inv = PIL.ImageOps.invert(image2)
#
# # Make the images of uniform size
# image3 = changeImageSize(800, 500, image1)
# image4 = changeImageSize(800, 500, image2)
#
# image4_inv = changeImageSize(800, 500, image2_inv)
#
# # Make sure images got an alpha channel
# image5 = image3.convert("RGBA")
# image6 = image4.convert("RGBA")
#
# image6_inv = image4_inv.convert("RGBA")
#
# # Display the images
# image5.show()
# image6.show()
#
# # alpha-blend the images with varying values of alpha
#
# alphaBlended1 = Image.blend(image5, image6, alpha=.2)
# alphaBlended3 = Image.blend(alphaBlended1, image6_inv, alpha=.8)
#
# alphaBlended2 = Image.blend(image5, image6, alpha=.4)
#
# # Display the alpha-blended images
# alphaBlended1.show()
# alphaBlended2.show()
#
# alphaBlended3.show()
