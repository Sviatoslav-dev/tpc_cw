from PIL import Image

im = Image.open(r"image.jpg")

width, height = im.size
print(im.size)

# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5

im1 = im.crop((width - 2048, height - 2048, width, height))
print(im1.size)
im1.save(r"image_2048x2048.jpg")
im1.show()

newsize = (512, 512)
im1 = im1.resize(newsize)
im1.save(r"image_512x512.jpg")
im1.show()
