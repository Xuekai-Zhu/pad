def solution():
    starting_weight = 80.0
    days = 4

    # Reduce the weight of the soup by half each day
    current_weight = starting_weight / (2 ** days)

    result = current_weight
    return result

print(solution())