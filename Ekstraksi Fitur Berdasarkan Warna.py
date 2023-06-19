import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, channel = image.shape

hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768), dtype=np.int32)

def makeItZero():
    for x in range(0, 256):
        hgr[x] = 0
        hgg[x] = 0
        hgb[x] = 0
for x in range(0, 768):
    hgrgb[x] = 0

makeItZero()

# th = int(256/64)
temp = [0]
for y in range(0, height):
    for x in range(0, width):
        red = int(image[y][x][0])
        green = int(image[y][x][1])
        blue = int(image[y][x][2])
        red = red + 0
        green = green + 256
        blue = blue + 512
        # temp.append(green)
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1
binsrgb = np.linspace(0, 768, 100)

binsr = np.linspace(0, 0, 100)
plt.hist(hgr, binsr, color = "red", alpha=0.5)
binsg = np.linspace(0, 256, 100)
plt.hist(hgr, binsg, color = "green", alpha=0.5)
binsb = np.linspace(0, 768, 100)
plt.hist(hgr, binsb, color = "blue", alpha=0.5)
#plt.hist(hgr, binsrgb, alpha=0.5)
plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")
plt.show()

hist_image = cv2. calcHist([image], [0], None, [768], [0, 768])
plt.plot(hist_image)
plt.title("Histogram Red Green Blue")
plt.show()

makeItZero()
for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        red = image[y][x][0]
        green = image[y][x][1]
        blue = image[y][x][2]
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1
def plot_result(red, green, blue):
    bins = np.linspace(0, 256, 128)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
    for ax in [ax1, ax2, ax3]:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.grid(color='b', linestyle='--', linewidth=0.5, alpha=0.3)
        ax.tick_params(direction='out', color='b', width='1')
    ax1.set_title('Red')
    ax2.set_title('Green')
    ax3.set_title('Blue')
    ax1.hist(red, bins, color="red", alpha=1)
    ax2.hist(green, bins, color="green", alpha=1)
    ax3.hist(blue, bins, color="blue", alpha=1)
plt.rcParams['figure.figsize'] = [20, 7]
plot_result(hgr, hgg, hgb)