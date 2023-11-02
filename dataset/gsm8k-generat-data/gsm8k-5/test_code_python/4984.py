def solution():
    # Let x be the number of years of experience Bill had 5 years ago
    x = 5

    # Calculate Joan's years of experience 5 years ago
    y = 3 * x

    # Calculate their current years of experience
    current_bill = x + 5
    current_joan = y + 5

    # Set up the equation for their current years of experience
    # current_joan = 2 * current_bill
    # Substitute current_bill = x + 5
    # current_joan = 2 * (x + 5)
    # current_joan = 2x + 10

    # Solve for x
    x = (current_joan - 10) / 2
    result = x
    return result

print(solution())