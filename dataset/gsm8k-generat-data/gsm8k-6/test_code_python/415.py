def solution():
    # Calculate the dog's weight at 9 weeks old
    weight_9_weeks = 6 * 2  # the puppy doubled in weight by week 9

    # Calculate the dog's weight at 3 months old
    weight_3_months = weight_9_weeks * 2  # the puppy doubled in weight again at 3 months old

    # Calculate the dog's weight at 5 months old
    weight_5_months = weight_3_months * 2  # the puppy doubled in weight again at 5 months old

    # Calculate the dog's final weight at one year old
    final_weight = weight_5_months + 30  # the dog reached its final adult weight by adding another 30 pounds

    result = final_weight
    return result

print(solution())