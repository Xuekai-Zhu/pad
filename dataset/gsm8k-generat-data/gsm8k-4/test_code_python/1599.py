def solution():
    """Natalie has $26 to go shopping. She bought a jumper for $9, a T-shirt for $4, and a pair of heels for $5. How much money does Natalie have left?"""
    # Define the initial amount of money Natalie has
    initial_amount = 26

    # Define the cost of the items Natalie bought
    jumper_cost = 9
    tshirt_cost = 4
    heels_cost = 5

    # Calculate the total cost of the items
    total_cost = jumper_cost + tshirt_cost + heels_cost

    # Calculate the amount of money Natalie has left
    remaining_amount = initial_amount - total_cost

    # Return the result
    result = remaining_amount
    return result

print(solution())