def solution():
    # Calculate the total number of sack lunches needed
    total_lunches = 35 + 5 + 1 + 3  # 35 children, 5 chaperones, 1 teacher, and 3 extra lunches

    # Calculate the total cost of all the lunches
    total_cost = total_lunches * 7  # each sack lunch costs $7
    result = total_cost
    return result

print(solution())