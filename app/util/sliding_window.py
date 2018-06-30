from PIL import Image
import os


def slide(image_path, window_width, window_height, w_offset, h_offset):
    image = Image.open(image_path)
    image_width = image.size[0]
    image_height = image.size[1]
    start_x = 0
    start_y = 0
    i = 0
    cut_result = {}

    if start_y + window_height > image_height:
        rate = window_width/window_height
        window_height = image_height
        window_width = window_height * rate

    if start_x + window_width > image_width:
        rate = window_width / window_height
        window_width = image_width
        window_height = window_width/rate

    while start_y + window_height <= image_height:
        while start_x + window_width <= image_width:
            image_cut = image.crop((start_x, start_y, start_x + window_width, start_y + window_height))
            cut_path = './doc/SlideWindowCuts/' + str(i) + "." + image_path.split('.')[-1]
            image_cut.save(cut_path)
            cut_result[cut_path] = {'startX': start_x, 'startY': start_y, 'endX': (start_x + window_width), 'endY': (start_y + window_height)}
            start_x += (w_offset*window_width)
            i += 1
        start_y += (h_offset+window_height)
        start_x = 0

    return cut_result


def clear_cut():
    sliding_window_path = "./doc/SlideWindowCuts/"
    cut_list = os.listdir(sliding_window_path)
    for i in range(0, len(cut_list)):
        path = os.path.join(sliding_window_path, cut_list[i])
        os.remove(path)