def solution():
    # Calculate the total amount raised so far
    total_raised = (10 * 25) + (7 * 50) + (1 * 100)

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = 750 - total_raised
    result = remaining_amount
    return result

print(solution())