from PIL import Image, ImageDraw


# MADE BY PAUL ZANOLIN
# This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.



# =============  CONFIG  =============
lines = []
# pour faire les connections, changer le background

colors = {
    "r": (244, 76, 61),
    "g": (0,255,0),
    "b": (51, 181, 221),
    "o": (221,140,0),
    "w": (255,255,255)
}

data = ["01000100b", "01100101w", "01110011b", "01110000o", "01101111o", "01101001r", "01101110r", "01110100r"]

drawLines = True
testMode = True

# =============  END     =============

def drawImage():
    # for test purpose
    if testMode:
        im = Image.open("baseTestSansLeGrisMoche.png")
    else:
        im = Image.open("base.png")

    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    im = im.rotate(-90)

    d = ImageDraw.Draw(im)

    color = (51, 181, 221)  # classic blue
    borderL = 33

    for i in range(8):
        for j in colors:
            if data[i][8] == j:
                color = colors[j]
        for j in range(8):
            if data[i][j] == "0":
                # full the circle
                for f in range(25):
                    cornerTLeft = (200 + 200 * i + borderL + f * 8, 200 + 200 * j + borderL + f * 8)
                    # topLeft (border + espacement * numcolone + borderL+ un peu plus pour remplir le cercle)
                    cornerBRight = (400 + 200 * i - borderL - f * 8, 400 + 200 * j - borderL - f * 8)
                    # bottomRight
                    d.arc([cornerTLeft, cornerBRight], 0, 360, color, 10)

    if drawLines:
        for line in lines:
            for j in colors:
                if line[4] == j:
                    color = colors[j]
            d.line([(300 + int(line[0]) * 200, 300 + int(line[1]) * 200),
                    (300 + int(line[2]) * 200, 300 + int(line[3]) * 200)], color, 200 - 2 * borderL)

    im = im.rotate(90)
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    #im.show()
    im.save("end.png")

inp = "noInput"
while(inp != "stop"):
    drawImage()
    print("\nAdd line: 'xxyyc' with  xx, yy coordinates, and c the color in dictionary")
    print("Delete line: 'xxyy' with  xx, yy coordinates")
    print("Change line color: 'xc' with  x line number and c the color in dictionary")
    print("stop to stop\n")
    inp = input()
    if(len(inp) == 5):
        part1 = inp[0:4]
        part2 = inp[4]
        if(part1.isdigit()):
            p1x = int(part1[0])
            p1y = int(part1[1])
            p2x = int(part1[2])
            p2y = int(part1[3])
            if(p1x >= 0 and p1x <= 7 and p1y >= 0 and p1y <= 7):
                if(p2x >= 0 and p2x <= 7 and p2y >= 0 and p2y <= 7):
                    if(part2 in colors):
                        lines.append(inp)
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    elif(len(inp) == 4):
        if(inp.isdigit()):
            p1x = int(inp[0])
            p1y = int(inp[1])
            p2x = int(inp[2])
            p2y = int(inp[3])
            if(p1x >= 0 and p1x <= 7 and p1y >= 0 and p1y <= 7):
                if(p2x >= 0 and p2x <= 7 and p2y >= 0 and p2y <= 7):
                    for line in lines:
                        if(inp == line[0:4]):
                            lines.remove(line)
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            if(inp == "stop"):
                testMode = False
                drawImage()
            else:
                print("Invalid Input")
    elif(len(inp) == 2):
        if(inp[0].isdigit()):
            i = int(inp[0])
            if(i >= 0 and i <= 8):
                if(inp[1] in colors):
                    data[i] = data[i][:8]+inp[1]