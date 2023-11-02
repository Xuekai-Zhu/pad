def solution():
    total_weight = 36  # Alex had 36 ounces of jelly beans
    weight_eaten = 6  # Alex ate 6 ounces of jelly beans

    # Calculate the weight of jelly beans remaining
    remaining_weight = total_weight - weight_eaten

    # Divide the remaining weight equally into 3 piles
    weight_per_pile = remaining_weight / 3
    result = weight_per_pile
    return result

print(solution())