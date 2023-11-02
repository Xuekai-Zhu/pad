def solution():
    weight_of_box = 2000  # 2 kilogram box of chocolate
    weight_of_one_bar = 125  # Chocolate bar weighs 125 g

    # Calculate the number of bars in the box
    num_of_bars = weight_of_box // weight_of_one_bar

    result = num_of_bars
    return result

print(solution())