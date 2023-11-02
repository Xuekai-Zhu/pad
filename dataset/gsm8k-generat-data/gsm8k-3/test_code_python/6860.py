def solution():
    """Calvin signed up for a gym training service to lose some pounds. If he weighed 250 pounds to start with and lost 8 pounds every month during the training sessions, what's his weight after one year?"""
    # Define Calvin's initial weight and the amount of weight he loses each month
    INITIAL_WEIGHT = 250
    MONTHLY_WEIGHT_LOSS = 8

    # Calculate Calvin's weight after one year
    final_weight = INITIAL_WEIGHT - (MONTHLY_WEIGHT_LOSS * 12)

    # Display Calvin's weight after one year
    result = final_weight
    return result

print(solution())