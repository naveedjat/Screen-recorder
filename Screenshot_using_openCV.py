import pyscreenshot

#----------------------FULL SCREENSHOT ----------------------------
# To capture the screen
# image = pyscreenshot.grab()
X = int(input("give the value of width: "))
Y = int(input("give the value of height: "))

image = pyscreenshot.grab(bbox=(10, 10, X,Y ))
# To display the captured screenshot
image.show()
# To save the screenshot
image.save("screenshot.png")

#---------------
