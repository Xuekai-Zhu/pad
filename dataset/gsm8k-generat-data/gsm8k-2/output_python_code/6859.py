def solution():
    """Calvin signed up for a gym training service to lose some pounds. If he weighed 250 pounds to start with and lost 8 pounds every month during the training sessions, what's his weight after one year?"""
    starting_weight = 250
    monthly_loss = 8
    total_loss = monthly_loss * 12
    final_weight = starting_weight - total_loss
    result = final_weight
    return result

print(solution())