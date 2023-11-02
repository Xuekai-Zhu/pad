def solution():
    # Define the amount raised by each family type
    family_20 = 2 * 20
    family_10 = 8 * 10
    family_5 = 10 * 5

    # Calculate the total amount raised by Classroom A
    total_raised = family_20 + family_10 + family_5

    # Calculate the amount still needed to reach the goal
    amount_needed = 200 - total_raised
    result = amount_needed
    return result

print(solution())