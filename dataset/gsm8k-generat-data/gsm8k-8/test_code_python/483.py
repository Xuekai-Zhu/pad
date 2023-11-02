def solution():
    # Calculate Andy's new weight after gaining weight and growing
    starting_weight = 156
    weight_gain = 36
    new_weight = starting_weight + weight_gain

    # Calculate how much weight Andy lost each month
    weight_lost_per_month = new_weight / 8
    weight_lost_total = weight_lost_per_month * 3

    # Calculate Andy's current weight
    current_weight = new_weight - weight_lost_total

    # Calculate how much less Andy weighs now than at the beginning of the year
    weight_difference = starting_weight - current_weight
    result = weight_difference
    return result

print(solution())