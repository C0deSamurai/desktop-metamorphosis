def average(x):
    return sum(x) / len(x)


def get_average_color(im):
    """Gets the average color, in RGB format, of the bandwise average
    of the colors in the image."""
    try:
        r, g, b = list(zip(*im.getdata()))
        return tuple([average(x) for x in (r, g, b)])
    except ValueError:
        print(im.format, im.mode)
        print("Big problem!")
