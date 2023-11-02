def solution():
    """The GooGoo brand of clothing manufactures two types of shirts, one with 3 buttons and the other with 5 buttons. A large department store ordered GooGoo to manufacture 200 of each type of shirt. How many buttons will the GooGoo brand use to manufacturer all of the shirts for this order?"""
    
    # Define the number of shirts ordered
    shirts_ordered = 200
    
    # Define the number of buttons on each type of shirt
    buttons_on_3button_shirt = 3
    buttons_on_5button_shirt = 5
    
    # Calculate the total number of buttons used to make all the shirts
    total_buttons_used = (shirts_ordered * buttons_on_3button_shirt) + (shirts_ordered * buttons_on_5button_shirt)
    
    # Return the result
    return total_buttons_used

print(solution())