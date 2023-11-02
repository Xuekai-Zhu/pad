def solution():
    # Calculate the volume of a widget, carton, and shipping box
    widget_volume = 4 * 4 * 5  # widget is 4 inches wide, 4 inches long, and 5 inches tall
    carton_volume = 3 * widget_volume  # each carton has 3 widgets
    shipping_box_volume = 20 * 20 * 20

    # Calculate the number of widgets that can fit in each shipping box
    widgets_per_box = shipping_box_volume // carton_volume
    result = widgets_per_box
    return result

print(solution())