def solution():
    """The GooGoo brand of clothing manufactures two types of shirts, one with 3 buttons and the other with 5 buttons. A large department store ordered GooGoo to manufacture 200 of each type of shirt. How many buttons will the GooGoo brand use to manufacturer all of the shirts for this order?"""
    buttons_per_shirt1 = 3
    buttons_per_shirt2 = 5
    shirts1 = 200
    shirts2 = 200
    total_buttons = (buttons_per_shirt1 * shirts1) + (buttons_per_shirt2 * shirts2)
    result = total_buttons
    return result

print(solution())