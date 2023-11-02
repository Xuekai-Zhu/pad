def solution():
    
    # Define Mark's initial weight and the weight loss per month
    initial_weight = 70
    weight_loss_per_month = 10

    # Calculate Mark's final weight after 3 months
    final_weight = initial_weight - (weight_loss_per_month * 3)

    # Display Mark's final weight
    result = final_weight
    return result

print(solution())