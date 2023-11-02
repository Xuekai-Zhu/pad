def solution():
    bike_cost = 112
    num_weeks = 2
    num_days = num_weeks * 7
    bracelet_cost = 1

    # Calculate the total amount of money Trey needs to raise
    total_money_needed = bike_cost

    # Calculate the total amount of money Trey can earn from bracelet sales
    total_money_earned = num_days * bracelet_cost

    # Calculate the number of bracelets Trey needs to sell each day
    num_bracelets_needed = total_money_needed / total_money_earned
    result = num_bracelets_needed
    return result

print(solution())