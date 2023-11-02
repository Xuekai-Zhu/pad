def solution():
    # Calculate the weight at 9 weeks old
    weight_at_9_weeks = 6 * 2 * 2  # Doubled in weight at week 9

    # Calculate the weight at 3 months old
    weight_at_3_months = weight_at_9_weeks * 2   # Doubled in weight at 3 months old

    # Calculate the weight at 5 months old
    weight_at_5_months = weight_at_3_months * 2   # Doubled in weight at 5 months old

    # Calculate the final adult weight
    final_weight = weight_at_5_months + 30   # Added another 30 pounds by the time it was one year old

    result = final_weight
    return result

print(solution())