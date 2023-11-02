def solution():
    """James replaces the coffee for the household. There are 3 other people in the house and everyone drinks 2 cups of coffee a day. It takes .5 ounces of coffee per cup of coffee. If coffee costs $1.25 an ounce, how much does he spend on coffee a week?"""
    # Define the number of people in the house and the number of cups of coffee each person drinks per day
    num_people = 4
    num_cups_per_person = 2
    num_cups_per_day = num_people * num_cups_per_person

    # Define the amount of coffee used per cup of coffee
    coffee_per_cup = 0.5 # in ounces

    # Define the cost of coffee per ounce
    coffee_cost_per_ounce = 1.25 # in dollars

    # Calculate the total amount of coffee used per day
    total_coffee_per_day = num_cups_per_day * coffee_per_cup # in ounces

    # Calculate the total cost of coffee per day
    total_cost_per_day = total_coffee_per_day * coffee_cost_per_ounce # in dollars

    # Calculate the total cost of coffee per week
    total_cost_per_week = total_cost_per_day * 7 # in dollars

    # return the result
    result = total_cost_per_week
    return result

print(solution())