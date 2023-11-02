def solution():
    weight_of_box = 2000  # in grams
    weight_of_bar = 125  # in grams

    # Calculate the number of bars in the box
    num_bars = weight_of_box // weight_of_bar

    result = num_bars
    return result

print(solution())