def solution():
    # Define the sum of the two numbers
    total_sum = 33

    # Define the ratio between the second number and the first number
    second_to_first_ratio = 2

    # Set up a system of equations to solve for both numbers
    # x + y = total_sum
    # y = second_to_first_ratio * x
    # Substitute the second equation into the first and solve for x
    x = total_sum / (1 + second_to_first_ratio)
    # Use the ratio to solve for y
    y = second_to_first_ratio * x

    # Return the second number
    result = y
    return result

print(solution())