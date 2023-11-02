def solution():
    """Doris works at the Widget Factory in the packing department. She puts 3 widgets in each carton, which are 4 inches wide, 4 inches long, and 5 inches tall. She then packs those cartons into a shipping box before sending it to the loading bay. The shipping boxes are 20 inches wide, 20 inches long, and 20 inches high. How many widgets get shipped in each shipping box?"""
    widgets_per_carton = 3
    carton_width = 4
    carton_length = 4
    carton_height = 5
    shipping_box_width = 20
    shipping_box_length = 20
    shipping_box_height = 20
    cartons_per_layer = (shipping_box_width // carton_width) * (shipping_box_length // carton_length)
    layers_per_box = shipping_box_height // carton_height
    widgets_per_box = cartons_per_layer * layers_per_box * widgets_per_carton
    result = widgets_per_box
    
    return result

print(solution())