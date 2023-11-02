def solution():
    number_of_people = 35 + 5 + 1 + 3  # Janet is picking up lunch for 35 children, 5 chaperones, herself, and 3 extra lunches
    cost_per_lunch = 7  # Each sack lunch costs $7

    # Calculate the total cost of all the lunches
    total_cost = number_of_people * cost_per_lunch
    result = total_cost
    return result

print(solution())