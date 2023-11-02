def solution():
    eggs_cost = 3  # Eggs cost $3
    pancakes_cost = 2  # Pancakes cost $2
    cocoa_cost = 2  # Mugs of cocoa cost $2 each
    num_cocoa = 2  # They order 2 mugs of cocoa initially
    tax = 1  # The tax is $1

    # Calculate the total cost of their initial order
    initial_cost = (eggs_cost + pancakes_cost + (cocoa_cost * num_cocoa)) + tax

    # Calculate the total cost of Ben's additional order
    additional_pancakes_cost = pancakes_cost  # Ben orders 1 more batch of pancakes
    additional_cocoa_cost = cocoa_cost  # Ben orders 1 more mug of cocoa
    additional_order_cost = additional_pancakes_cost + additional_cocoa_cost

    # Calculate the total cost of their entire order
    total_cost = initial_cost + additional_order_cost

    # Calculate the change they should get from $15
    change = 15 - total_cost
    result = change
    return result

print(solution())