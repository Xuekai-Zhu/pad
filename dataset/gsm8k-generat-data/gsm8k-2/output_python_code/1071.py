def solution():
    """The GooGoo brand of clothing manufactures two types of shirts, one with 3 buttons and the other with 5 buttons. A large department store ordered GooGoo to manufacture 200 of each type of shirt. How many buttons will the GooGoo brand use to manufacturer all of the shirts for this order?"""
    type1_buttons = 3
    type2_buttons = 5
    type1_quantity = 200
    type2_quantity = 200
    total_buttons = (type1_buttons * type1_quantity) + (type2_buttons * type2_quantity)
    result = total_buttons
    return result

print(solution())