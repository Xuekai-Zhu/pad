def solution():
    # Calculate the value of a single gold quarter if spent in store
    value_spent = 0.25

    # Calculate the value of a single gold quarter if melted down
    weight_quarter = 1/5  # weight of a single gold quarter in ounces
    value_melted = 100 * weight_quarter

    # Calculate the ratio of melted value to spent value
    ratio = value_melted / value_spent

    result = ratio
    return result

print(solution())