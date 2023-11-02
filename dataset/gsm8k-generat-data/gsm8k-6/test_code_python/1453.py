def solution():
    # Calculate the number of chocolate bars in a 2 kg box
    weight_per_bar = 125  # grams
    total_weight = 2000  # grams in 2 kg
    bars_in_box = total_weight // weight_per_bar
    result = bars_in_box
    return result

print(solution())