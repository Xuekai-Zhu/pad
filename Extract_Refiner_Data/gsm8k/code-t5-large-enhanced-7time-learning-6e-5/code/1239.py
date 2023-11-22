def solution():
    
    # Define the number of sticks and the cost per bag
    STICKS_PER_BAG = 30
    COST_PER_BAG = 18

    # Calculate the cost of the sticks before the discount
    cost_before_discount = STICKS_PER_BAG * COST_PER_BAG

    # Calculate the cost of the sticks after the discount
    cost_after_discount = cost_before_discount - 3

    # Calculate the cost per stick after the discount
    cost_per_stick = cost_after_discount / STICKS_PER_BAG

    # Convert the cost per stick to cents
    cost_per_stick_cents = cost_per_stick * 100

    # Display the cost per stick
    result = cost_per_stick_cents
    return result

print(solution())