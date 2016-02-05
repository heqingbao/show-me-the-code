from PIL import Image, ImageDraw, ImageFilter, ImageFont
import string
import random

def randomChar():
    return random.choice(string.letters)

def randomColor():
	return (random.randint(100, 225), random.randint(100, 225), random.randint(100, 225))

def randomColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60

image = Image.new(mode="RGB", size=(width, height), color=128)

draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=randomColor())

font = ImageFont.truetype("/Library/Fonts/arial.ttf", 36)

for i in range(4):
	draw.text((60 * i + 10, 10), randomChar(), font = font, fill=randomColor2())

del draw

image = image.filter(ImageFilter.BLUR)
image.show()

