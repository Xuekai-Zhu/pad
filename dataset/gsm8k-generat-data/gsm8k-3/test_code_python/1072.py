def solution():
    """The GooGoo brand of clothing manufactures two types of shirts, one with 3 buttons and the other with 5 buttons.  A large department store ordered GooGoo to manufacture 200 of each type of shirt.  How many buttons will the GooGoo brand use to manufacturer all of the shirts for this order?"""
    # Define the number of each type of shirt ordered
    num_3_button_shirts = 200
    num_5_button_shirts = 200

    # Define the number of buttons on each type of shirt
    num_buttons_3 = 3
    num_buttons_5 = 5

    # Calculate the total number of buttons needed for the order
    total_buttons = num_3_button_shirts * num_buttons_3 + num_5_button_shirts * num_buttons_5

    # Display the total number of buttons needed
    result = total_buttons
    return result

print(solution())