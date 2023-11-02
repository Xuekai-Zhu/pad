def solution():
    # Define the cost of the pencil as x
    x = 1

    # Define the cost of the pen as 2x
    pen_cost = 2*x

    # Calculate the total cost of the pen and pencil
    total_cost = pen_cost + x

    # Use the given information that the total cost is $6 to find the value of x
    x = (6 - pen_cost) / 2

    # Calculate the cost of the pen
    pen_cost = 2*x
    result = pen_cost
    return result

print(solution())