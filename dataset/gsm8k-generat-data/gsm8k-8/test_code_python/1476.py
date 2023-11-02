def solution():
    # Calculate Megan's weight
    kelly_weight = 34
    megan_weight = kelly_weight / 0.85

    # Calculate Mike's weight
    mike_weight = megan_weight + 5

    # Calculate total weight of the three children
    total_weight = kelly_weight + megan_weight + mike_weight

    # Calculate excess weight
    excess_weight = total_weight - 100
    result = excess_weight
    return result

print(solution())