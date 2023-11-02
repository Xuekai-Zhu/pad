def solution():
    """Calvin signed up for a gym training service to lose some pounds. If he weighed 250 pounds to start with
     and lost 8 pounds every month during the training sessions, what's his weight after one year?"""
    # Define the initial weight and the weight loss per month
    initial_weight = 250
    weight_loss_per_month = 8

    # Calculate the weight after one year
    weight_after_one_year = initial_weight - (weight_loss_per_month * 12)

    # Return the result
    result = weight_after_one_year
    return result

print(solution())