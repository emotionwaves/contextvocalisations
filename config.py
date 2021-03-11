import os
import numpy as np

# Colors for each point in HTML.
pastel = [
    "#ff5f00", "#00FFFF", "#6AFB92", "#FFFF00", "#F62217",
    "#FF00FF", "#F9B7FF"]

# shuffle colors so classes have distinct colors when fewer
np.random.seed(320)
np.random.shuffle(pastel)

rainbow = [
    "#ff5f00", "#00FFFF", "#6AFB92", "#FFFF00", "#F62217",
    "#FF00FF", "#F9B7FF"]

COLOR_LIST = pastel

# Symbols to be used for points in HTML.
symbol_list = ["&#%d;"%i for i in range(913, 1014)] # Greek and Coptic

SYMBOL_LIST= ["&#%d;"%i for i in range(9642, 9727)] + symbol_list # geometrical shapes

POINT_TEMPLATE = "<div id=item{item_index} class=\"genre\" scan=true style=\"color: {color_hex}; font-size: 350%; top: {button_x}px; left: {button_y}px;\" onmouseover=\"playx(&quot;{file_name}&quot;, &quot;{item_index}&quot;,[], this);\" title=\"{class_label}\"><b>{item_symbol}</b></div>"

LABEL_TEMPLATE = '<div class="embossed" style="position: static; color: {class_color}; top: {class_label_x}px; left: {class_label_y}px; font-size: 130%"><b>{label_symbol}-{class_label}</b></div>'
