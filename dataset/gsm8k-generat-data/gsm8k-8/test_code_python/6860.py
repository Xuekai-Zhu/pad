def solution():
    # Define initial weight and weight loss per month
    initial_weight = 250
    weight_loss_per_month = 8

    # Calculate weight after one year (12 months)
    final_weight = initial_weight - (weight_loss_per_month * 12)
    result = final_weight
    return result

print(solution())