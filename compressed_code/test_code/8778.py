def solution():
    
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