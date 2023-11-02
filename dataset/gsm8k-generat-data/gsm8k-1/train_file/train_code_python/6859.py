def solution():
    """Calvin signed up for a gym training service to lose some pounds. If he weighed 250 pounds to start with and lost 8 pounds every month during the training sessions, what's his weight after one year?"""
    starting_weight = 250
    pounds_lost_per_month = 8
    months_in_a_year = 12
    total_pounds_lost = pounds_lost_per_month * months_in_a_year
    final_weight = starting_weight - total_pounds_lost
    result = final_weight
    return result

print(solution())