def solution():
    # Determine the volume of each carton
    carton_volume = 4 * 4 * 5

    # Determine the maximum number of cartons that can fit in the shipping box
    shipping_box_volume = 20 * 20 * 20
    max_cartons_per_box = shipping_box_volume // carton_volume

    # Determine the number of widgets in each box
    widgets_per_carton = 3
    widgets_per_box = max_cartons_per_box * widgets_per_carton
    result = widgets_per_box
    return result

print(solution())