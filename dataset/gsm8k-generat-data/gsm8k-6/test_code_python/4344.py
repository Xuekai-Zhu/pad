def solution():
    # Calculate the total value of the other 8 toys
    total_value_other_toys = 52 - 12  # one toy is worth $12
    # Calculate the value of one of the other toys
    price_of_one_other_toy = total_value_other_toys / 8
    result = price_of_one_other_toy
    return result

print(solution())