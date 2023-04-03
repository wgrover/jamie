#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys, os

dpi = 300
margin = 0.1  # inches

margin = margin * dpi  # margin in dpi
width = 3*dpi
height = 2*dpi
maxwidth = width - 2 * margin
maxheight = height - 2 * margin
bestfontsize = 1
bestwidth = 1
bestheight = 1
bestmessage = ""

img = Image.new('RGB', (width, height), color='white')
imgDraw = ImageDraw.Draw(img)

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = "Depleted uranium"  # a test message

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
        left, top, right, bottom = imgDraw.multiline_textbbox((0,0), testmessage, font=ImageFont.truetype("FreeSansBold.ttf", size=fontsize, layout_engine=ImageFont.Layout.BASIC))
        textWidth, textHeight = right - left, bottom - top
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
imgDraw.multiline_text((width/2, height/2), bestmessage, font=ImageFont.truetype("FreeSansBold.ttf",
              size=bestfontsize, layout_engine=ImageFont.Layout.BASIC), fill=(0,0,0), align="center", anchor="mm")
img.save('label.png')
if len(sys.argv) > 1:  # don't print the test message
    os.system("lpr -P iDPRT_SP410 -o media=Custom.3x2in label.png")
