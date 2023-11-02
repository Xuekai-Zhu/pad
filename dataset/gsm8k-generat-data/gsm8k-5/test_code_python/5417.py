def solution():
    starting_weight = 99  # Mary weighed 99 pounds at the start of her diet

    # Calculate how much weight Mary lost and gained
    weight_lost = 12
    weight_gained_back = 2 * weight_lost
    weight_lost_again = 3 * weight_lost
    weight_gained_back_again = 6

    # Calculate Mary's final weight
    final_weight = starting_weight - weight_lost + weight_gained_back - weight_lost_again + weight_gained_back_again
    result = final_weight
    return result

print(solution())