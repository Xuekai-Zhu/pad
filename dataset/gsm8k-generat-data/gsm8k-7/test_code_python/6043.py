def solution():
    weight_per_quarter = 1/5  # ounce
    value_in_store = 0.25  # dollars per quarter
    value_per_ounce_melted = 100  # dollars per ounce

    # Calculate the value of all the quarters in a store
    total_value_in_store = value_in_store * num_quarters

    # Calculate the weight of all the quarters
    total_weight = weight_per_quarter * num_quarters

    # Calculate the value if they were melted down
    total_value_melted = total_weight * value_per_ounce_melted

    # Calculate the ratio of melted value to store value
    ratio = total_value_melted / total_value_in_store

    result = ratio
    return result

print(solution())