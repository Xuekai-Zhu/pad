def solution():
    starting_weight = 250  # Calvin weighed 250 pounds to start with
    pounds_lost_per_month = 8  # Calvin lost 8 pounds every month during the training sessions
    total_months = 12  # Calvin completed 12 months of training

    # Calculate Calvin's weight after one year of training
    final_weight = starting_weight - (pounds_lost_per_month * total_months)
    result = final_weight
    return result

print(solution())