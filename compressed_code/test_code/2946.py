def solution():
    
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