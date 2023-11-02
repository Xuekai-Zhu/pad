def solution():
    goal_per_classroom = 200

    # Calculate the total amount raised from each family
    fam1 = 20 * 2
    fam2 = 10 * 8
    fam3 = 5 * 10

    # Calculate the total amount raised by the classroom
    total_raised = fam1 + fam2 + fam3

    # Calculate the amount of money needed to reach the goal
    amount_needed = goal_per_classroom - total_raised
    result = amount_needed
    return result

print(solution())