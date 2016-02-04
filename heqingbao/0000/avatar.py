from PIL import Image, ImageDraw, ImageFont

im = Image.open("avatar.png");

draw = ImageDraw.Draw(im)

fnt = ImageFont.truetype("/Library/Fonts/Arial.ttf", size=36)
xy = (im.size[0] - 60, 20)
draw.text(xy, "10", font=fnt, fill=(255, 0, 0))

del draw

im.save("result.png", "PNG")

im.show()
