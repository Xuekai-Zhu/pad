def solution():
    gold_value = 100  # Carlos can get $100 per ounce for melted gold
    quarter_weight = 1/5  # Each quarter weighs 1/5 of an ounce
    quarter_value = 0.25  # The regular value of a quarter is $0.25

    # Calculate the value of the gold in one quarter
    gold_per_quarter = gold_value * quarter_weight

    # Calculate the ratio of melted gold value to regular value
    melted_ratio = gold_per_quarter / quarter_value

    result = melted_ratio
    return result

print(solution())