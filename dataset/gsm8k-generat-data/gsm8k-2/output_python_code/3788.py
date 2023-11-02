def solution():
    """Doris works at the Widget Factory in the packing department. She puts 3 widgets in each carton, which are 4 inches wide, 4 inches long, and 5 inches tall. She then packs those cartons into a shipping box before sending it to the loading bay. The shipping boxes are 20 inches wide, 20 inches long, and 20 inches high. How many widgets get shipped in each shipping box?"""
    carton_width = 4
    carton_length = 4
    carton_height = 5
    carton_volume = carton_width * carton_length * carton_height
    widgets_per_carton = 3
    shipping_width = 20
    shipping_length = 20
    shipping_height = 20
    shipping_volume = shipping_width * shipping_length * shipping_height
    cartons_per_shipping_box = shipping_volume // carton_volume
    widgets_per_shipping_box = cartons_per_shipping_box * widgets_per_carton
    result = widgets_per_shipping_box
    return result

print(solution())