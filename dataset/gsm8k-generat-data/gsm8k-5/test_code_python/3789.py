def solution():
    widget_dimensions = [4, 4, 5]  # Dimensions of each widget in inches
    carton_capacity = 3  # Each carton can hold 3 widgets
    shipping_box_dimensions = [20, 20, 20]  # Dimensions of the shipping box in inches

    # Calculate the volume of each widget in cubic inches
    widget_volume = 1
    for dim in widget_dimensions:
        widget_volume *= dim

    # Calculate the volume of each carton in cubic inches
    carton_volume = widget_volume * carton_capacity

    # Calculate the number of widgets that can fit in each shipping box
    shipping_box_volume = 1
    for dim in shipping_box_dimensions:
        shipping_box_volume *= dim
    widgets_per_box = shipping_box_volume // carton_volume

    result = widgets_per_box
    return result

print(solution())