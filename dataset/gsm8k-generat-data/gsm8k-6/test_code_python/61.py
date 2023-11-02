def solution():
    # Calculate the total weight gained by the bear
    total_weight_gained = (1/5) * 1000  # a fifth of the weight it needed from berries during summer
    total_weight_gained += 2 * (1/5) * 1000  # twice that amount from acorns during autumn
    total_weight_gained += (1/2) * (1000 - total_weight_gained)  # salmon made up half of the remaining weight

    # Calculate the weight gained from small animals
    weight_gained_from_small_animals = 1000 - total_weight_gained
    result = weight_gained_from_small_animals
    return result

print(solution())