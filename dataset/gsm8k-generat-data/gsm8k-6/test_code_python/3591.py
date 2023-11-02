def solution():
    # Calculate the value of Pima's Ethereum investment after two weeks
    week1_gain = 0.25 * 400  # value gained in first week
    week1_value = week1_gain + 400  # total value after first week
    week2_gain = 0.5 * week1_value  # value gained in second week
    total_value = week2_gain + week1_value  # total value after two weeks
    result = total_value
    return result

print(solution())