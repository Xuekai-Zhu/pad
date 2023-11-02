def solution():
    # Calculate the cost of supplies for one student
    cost_per_student = (5 * 0.5) + (3 * 1.25) + 4.25 + (2 * 0.75)

    # Calculate the total cost of supplies for the whole class
    total_cost = cost_per_student * 30

    # Apply the teacher discount
    discounted_cost = total_cost - 100

    result = discounted_cost
    return result

print(solution())