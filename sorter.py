from PIL import Image
from averagecolor import luminance
from os import makedirs
from pathlib import Path
from tqdm import tqdm


IMAGE_DIR = Path.cwd().joinpath("test")
IMAGE_FILETYPES = ("png", "jpg")
NUM_GROUPS = 2


def sort(im_dir=IMAGE_DIR, im_types=IMAGE_FILETYPES, num=NUM_GROUPS):
    makedirs("{}/sorted-images".format(im_dir), exist_ok=True)

    for i in range(num):
        makedirs("{}/sorted-images/sorted-{}".format(im_dir, i+1), exist_ok=True)
    image_paths = [pth for pth in Path(im_dir).iterdir()
                   if pth.suffix[1:] in im_types]

    top = 255
    thresholds = [top*i/num for i in range(1, num+1)]
    # print(thresholds)
    
    for pth in tqdm(iterable=image_paths, desc="Sorting images by brightness", unit="pic",
                    smoothing=0.15):
        im = Image.open(pth)
        im = im.convert("RGB")
        average = luminance(im)
        # print(average)
        # test for which "bucket" to throw the image in
        for i, threshold in enumerate(thresholds):
            diff = thresholds[1] - thresholds[0]
            if average <= threshold and (average+diff) >= threshold:
                im.save("{}/sorted-images/sorted-{}/{}".format(im_dir, i+1, pth.name))
                continue

    with open("{}/sorted-images/sorted.txt".format(im_dir), mode="w") as file:
        file.write("These files are sorted by luminosity.")
    print("Successful!")

if __name__ == "__main__":
    sort()
