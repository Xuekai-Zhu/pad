def solution():
    egg_price = 3
    pancake_price = 2
    cocoa_price = 2
    num_cocoas = 2
    tax = 1
    additional_pancakes = 1
    additional_cocoa = 1
    total_paid = 15

    # Calculate the total cost of the initial order
    initial_order_cost = egg_price + (pancake_price * 2) + (cocoa_price * num_cocoas) + tax

    # Calculate the total cost of the additional pancakes and cocoa that Ben ordered
    additional_cost = (pancake_price * additional_pancakes) + (cocoa_price * additional_cocoa)

    # Calculate the total amount paid for the meal
    total_cost = initial_order_cost + additional_cost

    # Calculate the change from the total amount paid
    change = total_paid - total_cost
    result = change
    return result

print(solution())