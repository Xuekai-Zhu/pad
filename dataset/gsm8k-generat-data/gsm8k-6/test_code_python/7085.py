def solution():
    # Calculate the total amount of money raised by Classroom A
    total_raised = 2*20 + 8*10 + 10*5

    # Calculate the amount of money still needed to reach the goal
    amount_needed = 200 - total_raised
    result = amount_needed
    return result

print(solution())