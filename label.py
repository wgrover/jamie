#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

dpi = 300
margin = 0.1  # inches

margin = margin * dpi  # margin in dpi
width = 3*dpi
height = 2*dpi
maxwidth = width - 2*margin
maxheight = height - 2*margin

img = Image.new('RGB', (width, height), color='white')
imgDraw = ImageDraw.Draw(img)

message = "Wire"


textWidth = 0
textHeight = 0
fontsize = 0
while textWidth < maxwidth and textHeight < maxheight:
    fontsize += 1
    font = ImageFont.truetype("FreeSansBold.ttf", size=fontsize)
    textWidth, textHeight = imgDraw.textsize(message, font=font)
print("winner winner chicken dinner", textWidth, textHeight)



imgDraw.text((width/2, height/2), message, font=ImageFont.truetype("FreeSansBold.ttf", size=fontsize),
              fill=(0,0,0), align="center", anchor="mm", spacing=-30)
img.save('label.png')