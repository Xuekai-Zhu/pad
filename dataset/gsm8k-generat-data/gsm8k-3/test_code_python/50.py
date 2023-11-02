def solution():
    """Gerald spends $100 a month on baseball supplies. His season is 4 months long. He wants to use the months he's not playing baseball to save up by raking, shoveling, and mowing lawns. He charges $10 for each. How many chores does he need to average a month to save up for his supplies?"""
    # Define the total cost of baseball supplies for the season
    supplies_cost = 100 * 4

    # Define the total amount Gerald wants to save up
    savings_goal = supplies_cost

    # Define the number of months Gerald will be saving up
    saving_months = 8

    # Calculate the total amount of money Gerald can earn from doing chores
    total_earnings = 10 * saving_months

    # Calculate the number of chores Gerald needs to average per month to reach his savings goal
    chores_per_month = (savings_goal - total_earnings) / saving_months / 10

    # Round up the number of chores
    result = math.ceil(chores_per_month)
    return result

print(solution())