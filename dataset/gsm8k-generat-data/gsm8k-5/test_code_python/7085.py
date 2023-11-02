def solution():
    # Calculate total amount raised so far by Classroom A
    total_raised = (20 * 2) + (10 * 8) + (5 * 10)  # $20 from 2 families, $10 from 8 families, $5 from 10 families

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = 200 - total_raised
    result = remaining_amount
    return result

print(solution())