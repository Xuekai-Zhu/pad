def solution():
    # Define the cost of the dress and the initial savings
    dress_cost = 80
    initial_savings = 20

    # Define the weekly allowance and arcade expenses
    weekly_allowance = 30
    arcade_expenses = 10

    # Calculate the total amount Vanessa can save each week
    total_savings_per_week = weekly_allowance - arcade_expenses

    # Calculate the total amount of weeks needed to save enough money
    total_saving_time = (dress_cost - initial_savings) / total_savings_per_week

    # Round up to the nearest whole week
    weeks_needed = math.ceil(total_saving_time)

    result = weeks_needed
    return result

print(solution())