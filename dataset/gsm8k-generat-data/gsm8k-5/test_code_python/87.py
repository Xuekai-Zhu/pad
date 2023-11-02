def solution():
    starting_weight = 400  # John's cow weighs 400 pounds
    final_weight = starting_weight * 1.5  # The cow's weight increases to 1.5 times its starting weight
    weight_gain = final_weight - starting_weight  # The cow gains this amount of weight
    price_per_pound = 3
    increase_in_value = weight_gain * price_per_pound  # The increase in value due to weight gain

    result = increase_in_value
    return result

print(solution())