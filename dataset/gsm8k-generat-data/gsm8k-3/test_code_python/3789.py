def solution():
    """Doris works at the Widget Factory in the packing department. She puts 3 widgets in each carton, which are 4 inches wide, 4 inches long, and 5 inches tall. She then packs those cartons into a shipping box before sending it to the loading bay. The shipping boxes are 20 inches wide, 20 inches long, and 20 inches high. How many widgets get shipped in each shipping box?"""
    # Define the dimensions of the carton and shipping box in inches
    CARTON_WIDTH = 4
    CARTON_LENGTH = 4
    CARTON_HEIGHT = 5
    SHIPPING_BOX_WIDTH = 20
    SHIPPING_BOX_LENGTH = 20
    SHIPPING_BOX_HEIGHT = 20

    # Calculate the number of cartons that fit in a shipping box
    cartons_per_box = (SHIPPING_BOX_WIDTH // CARTON_WIDTH) * (SHIPPING_BOX_LENGTH // CARTON_LENGTH) * (
            SHIPPING_BOX_HEIGHT // CARTON_HEIGHT)

    # Calculate the number of widgets in each shipping box
    widgets_per_box = cartons_per_box * 3

    # Display the number of widgets in each shipping box
    result = widgets_per_box
    return result

print(solution())