def solution():
    """Dakota and Ben order eggs for $3, pancakes for $2, and 2 mugs of cocoa for $2 each. The tax is $1. Later, Ben then decides to order 1 more batch of pancakes and 1 more mug of cocoa as he is still hungry. How much change should they get from $15?"""
    eggs_cost = 3
    pancakes_cost = 2
    cocoa_cost = 2
    num_cocoas = 2
    tax = 1
    subtotal = (eggs_cost + pancakes_cost + (cocoa_cost * num_cocoas)) + tax
    add_pancakes = 1
    add_cocoa = 1
    new_subtotal = subtotal + (add_pancakes * pancakes_cost) + (add_cocoa * cocoa_cost)
    change = 15 - new_subtotal
    result = change
    return result

print(solution())