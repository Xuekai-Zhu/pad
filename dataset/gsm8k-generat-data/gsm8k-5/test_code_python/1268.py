def solution():
    toothpaste_weight = 105  # The toothpaste contains 105 grams
    usage_per_brushing = 3 + 2 + 1 + 1  # The total usage per brushing by all family members
    brushings_per_day = 3  # Each family member brushes their teeth three times a day

    # Calculate the total usage per day
    usage_per_day = usage_per_brushing * brushings_per_day

    # Calculate the number of days the toothpaste will last
    days = toothpaste_weight / usage_per_day
    result = days
    return result

print(solution())