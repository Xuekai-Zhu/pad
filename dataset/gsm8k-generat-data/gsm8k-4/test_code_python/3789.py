def solution():
    """Doris works at the Widget Factory in the packing department. She puts 3 widgets in each carton, which are 4 inches wide, 4 inches long, and 5 inches tall. She then packs those cartons into a shipping box before sending it to the loading bay. The shipping boxes are 20 inches wide, 20 inches long, and 20 inches high. How many widgets get shipped in each shipping box?"""
    # Define the dimensions of the widget carton
    carton_width = 4
    carton_length = 4
    carton_height = 5

    # Calculate the volume of a single widget carton
    carton_volume = carton_width * carton_length * carton_height

    # Define the dimensions of the shipping box
    box_width = 20
    box_length = 20
    box_height = 20

    # Calculate the volume of the shipping box
    box_volume = box_width * box_length * box_height

    # Calculate the number of widget cartons that fit in a single shipping box
    cartons_per_box = box_volume // carton_volume

    # Calculate the number of widgets that fit in a single shipping box
    widgets_per_box = cartons_per_box * 3

    result = widgets_per_box
    return result

print(solution())