def solution():
    initial_weight = 80
    current_weight = initial_weight

    # Calculate the weight of the batch after each day
    for i in range(1, 5):
        current_weight = current_weight / 2

    result = current_weight
    return result

print(solution())