#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

dpi = 300
margin = 0.1  # inches

margin = margin * dpi  # margin in dpi
width = 3*dpi
height = 2*dpi
maxwidth = width - 2*margin
maxheight = height - 2*margin
bestfontsize = 1
bestwidth = 1
bestheight = 1
bestmessage = ""

img = Image.new('RGB', (width, height), color='white')
imgDraw = ImageDraw.Draw(img)

message = "wire wire wire wire wire"

words = message.split()
for seppattern in range(2**(len(words)-1)):
    testmessage = ""
    for w, word in enumerate(words):
        sep = " "
        if(2**w & seppattern):
            sep = "\n"
        testmessage += word + sep
    testmessage = testmessage.strip()  # get rid of terminal space
    textWidth = 1
    textHeight = 1
    fontsize = 0
    while textWidth < maxwidth and textHeight < maxheight:
        fontsize += 1
        textWidth, textHeight = imgDraw.textsize(testmessage, font=ImageFont.truetype("FreeSansBold.ttf", size=fontsize))
    print(repr(testmessage), fontsize, end="")
    if fontsize > bestfontsize:
        bestmessage = testmessage
        bestwidth = textWidth
        bestheight = textHeight
        bestfontsize = fontsize
        print(" <--- NEW BEST")
    else:
        print()

print("Making label with", repr(bestmessage))
imgDraw.text((bestwidth/2+margin, bestheight/2+margin), bestmessage, font=ImageFont.truetype("FreeSansBold.ttf",
              size=bestfontsize), fill=(0,0,0), align="center", anchor="mm", spacing=-30)
img.save('label.png')