from PIL import Image
from averagecolor import get_average_color
from os import makedirs
from pathlib import Path
from tqdm import tqdm


IMAGE_DIR = "/home/nicholas/Pictures/low-poly-backgrounds"
IMAGE_FILETYPES = ("png", "jpg")
NUM_GROUPS = 2


def luminance(r, g, b):
    """Gets the perceived luminance of the given color."""
    return (0.299*r + 0.587*g + 0.114*b)


def sort(im_dir=IMAGE_DIR, im_types=IMAGE_FILETYPES, num=NUM_GROUPS):
    for i in range(1, num+1):
        makedirs("{}/sorted-{}".format(im_dir, i), exist_ok=True)
    image_paths = [pth for pth in Path(im_dir).iterdir()
                   if pth.suffix[1:] in im_types]
    top = 255
    thresholds = [top*i/num for i in range(1, num+1)]
    # print(thresholds)
    
    for pth in tqdm(image_paths):
        im = Image.open(pth)
        im = im.convert("RGB")
        average = luminance(*get_average_color(im))
        # print(average)
        # test for which "bucket" to throw the image in
        for i, threshold in enumerate(thresholds):
            diff = thresholds[1] - thresholds[0]
            if average <= threshold and (average+diff) >= threshold:
                im.save("{}/sorted-{}/{}".format(im_dir, i+1, pth.name))
                continue

    with open("{}/sorted.txt".format(im_dir), mode="w") as file:
        file.write("Sorting has taken place")
    print("Successful!")

if __name__ == "__main__":
    sort()
