def solution():
    """Joy has 30 pencils, and Colleen has 50 pencils. If they bought the pencils at $4 each at the store, how much more money did Colleen pay than Joy for her pencils?"""
    # Define the number of pencils each person has
    joy_pencils = 30
    colleen_pencils = 50

    # Define the price per pencil
    pencil_price = 4

    # Calculate the total cost for Joy and Colleen
    joy_cost = joy_pencils * pencil_price
    colleen_cost = colleen_pencils * pencil_price

    # Calculate the difference in cost
    cost_difference = colleen_cost - joy_cost

    # Display the result
    result = cost_difference
    return result

print(solution())