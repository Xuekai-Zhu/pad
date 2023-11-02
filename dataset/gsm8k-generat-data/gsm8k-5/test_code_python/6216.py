def solution():
    previous_budget = 1000  # Let's assume the previous budget was $1000
    new_budget = previous_budget * 1.2  # Add 20% to the previous budget

    # Calculate the number of dodgeballs they can buy with the previous budget
    num_dodgeballs_prev = previous_budget // 5
    # Calculate the number of softballs they can buy with the new budget
    num_softballs_new = int(new_budget // 9)  # Round down to the nearest integer

    result = num_softballs_new
    return result

print(solution())