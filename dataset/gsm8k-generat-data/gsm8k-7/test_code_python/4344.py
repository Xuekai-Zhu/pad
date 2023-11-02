def solution():
    total_worth = 52
    num_toys = 9
    price_of_one_toy = 12

    # Calculate the total value of all the toys except one
    total_value_of_other_toys = total_worth - price_of_one_toy

    # Calculate the value of one of the other toys
    price_of_other_toy = total_value_of_other_toys / (num_toys - 1)
    result = price_of_other_toy
    return result

print(solution())