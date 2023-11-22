def solution():
    
    # Define Mark's final weight and the weight loss per month
    final_weight = 70
    weight_loss_per_month = 10

    # Calculate Mark's weight after 3 months of loss
    weight_after_loss = final_weight - (weight_loss_per_month * 3)

    # Calculate Mark's initial weight
    initial_weight = weight_after_loss + weight_loss_per_month

    # Display Mark's initial weight
    result = initial_weight
    return result

print(solution())