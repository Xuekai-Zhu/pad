def solution():
    widgets_per_carton = 3
    widget_width = 4
    widget_length = 4
    widget_height = 5
    shipping_box_width = 20
    shipping_box_length = 20
    shipping_box_height = 20

    # Calculate the volume of one widget
    widget_volume = widget_width * widget_length * widget_height

    # Calculate the volume of one carton
    carton_volume = widget_volume * widgets_per_carton

    # Calculate the maximum number of cartons that can fit in one shipping box
    max_cartons_per_box = (shipping_box_width * shipping_box_length * shipping_box_height) / carton_volume

    # Calculate the maximum number of widgets that can fit in one shipping box
    max_widgets_per_box = max_cartons_per_box * widgets_per_carton
    result = max_widgets_per_box
    return result

print(solution())