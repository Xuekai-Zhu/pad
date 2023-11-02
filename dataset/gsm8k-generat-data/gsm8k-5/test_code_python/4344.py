def solution():
    value_one_toy = 12  # One toy is worth $12
    total_value = 52  # The total value of all 9 toys is $52
    number_of_other_toys = 8  # There are 8 other toys with the same value

    # Calculate the total value of the other toys
    total_value_other_toys = total_value - value_one_toy

    # Calculate the value of one of the other toys
    value_each_other_toy = total_value_other_toys / number_of_other_toys
    result = value_each_other_toy
    return result

print(solution())