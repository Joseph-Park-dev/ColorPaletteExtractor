import math
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from PIL import Image, ImageDraw
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from collections import Counter

from colormap import rgb2hex

def color_to_df(input):
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    
    #convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                          int(i.split(", ")[1]),
                          int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
    
    df = pd.DataFrame(zip(df_color_up, df_percent), columns = ['c_code','occurence'])
    return df

def extract(input_image, output_image, bg_color, col_count):
    alpha_threshold = 1

    #background
    bg = 'bg.png'
    fig, ax = plt.subplots(figsize=(192,108),dpi=10)
    fig.set_facecolor('white')
    plt.savefig(bg)
    plt.close(fig)
    
    #resize
    resize = 1000
    output_width = resize
    img = Image.open(input_image).convert("RGBA")
    if img.size[0] >= resize:
        wpercent = (output_width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((output_width,hsize), Image.LANCZOS)
        resize_name = 'resize_.png'
        img.save(resize_name)
    else:
        resize_name = input_image

    width, height = img.size
    total_pixels = width * height
    
    #Get data
    img_url = resize_name
    pixels = list(img.getdata())

    # Filter out transparent pixels
    opaque = [
        (r, g, b)
        for r, g, b, a in pixels
        if a >= alpha_threshold
    ]

    if not opaque:
        raise ValueError("No opaque pixels found in image")

    counter = Counter(opaque)
    colors = counter.most_common(col_count)    

    rgbVals = list()
    percentages = list()

    for rgb, count in colors:
        rgbVals.append(tuple(val / 255 for val in rgb))
        percentages.append(round(count / total_pixels * 100, 1))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(160,120), dpi = 10)

    #donut plot
    wedges, text = ax1.pie(percentages,
                           labels= tuple(str(val) + "%" for val in percentages),
                           labeldistance= 1.05,
                           colors = rgbVals,
                           textprops={'fontsize': 150, 'color':'black'})
    plt.setp(wedges, width=0.3)

    #add image in the center of donut plot
    img = mpimg.imread(resize_name)
    imagebox = OffsetImage(img, zoom = True)
    ab = AnnotationBbox(imagebox, (0, 0))
    ax1.add_artist(ab)
    
    #color palette
    box_width = 100
    count = len(rgbVals)

    x_count = 5
    y_count = math.ceil(count / x_count)

    palette = Image.new('RGB', (box_width * x_count, box_width * y_count), bg_color)
    draw = ImageDraw.Draw(palette)

    for i in range (0, count):
        x = i % x_count
        y = math.floor(i / x_count)
        fill_color = tuple(int(x * 255) for x in rgbVals[i])
        draw.rectangle([(x * box_width, y * box_width), (x * box_width + box_width, y * box_width + box_width)], fill_color)

    palette.save(output_image)
    palette.show()

    x_posi, y_posi, y_posi2 = 160, -170, -170
    for c in rgbVals:
        color_str = tuple(round(x * 100, 1) for x in c)
        if rgbVals.index(c) <= 5:
            y_posi += 180
            rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor = c)
            ax2.add_patch(rect)
            ax2.text(x = x_posi+400, y = y_posi+100, s = color_str, fontdict={'fontsize': 190})
        else:
            y_posi2 += 180
            rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor = c)
            ax2.add_artist(rect)
            ax2.text(x = x_posi+1400, y = y_posi2+100, s = color_str, fontdict={'fontsize': 190})

    fig.set_facecolor('white')
    ax2.axis('off')
    bg = plt.imread('bg.png')
    plt.imshow(bg)       
    plt.tight_layout()

    if os.path.exists(img_url):
        os.remove(img_url)
    return plt.show()