def solution():
    """Trey is raising money for a new bike that costs $112. He plans to spend the next two weeks selling bracelets for $1 each. On average, how many bracelets does he need to sell each day?"""
    # Define the cost of the bike and the duration of time Trey has to sell bracelets
    bike_cost = 112
    selling_duration = 14  # days

    # Calculate the total amount of money Trey needs to raise
    total_money_needed = bike_cost

    # Calculate the amount of money Trey can raise by selling bracelets
    total_money_raised = selling_duration * 7 * 1  # 7 bracelets a day for 14 days, sold for $1 each

    # Calculate the number of bracelets Trey needs to sell each day
    bracelets_per_day = total_money_needed / total_money_raised
    result = round(bracelets_per_day, 1)
    return result

print(solution())