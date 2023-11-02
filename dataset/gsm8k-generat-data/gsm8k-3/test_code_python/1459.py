def solution():
    """James replaces the coffee for the household.  There are 3 other people in the house and everyone drinks 2 cups of coffee a day.  It takes .5 ounces of coffee per cup of coffee.  If coffee costs $1.25 an ounce, how much does he spend on coffee a week?"""
    # Define the number of people in the house and the number of cups of coffee consumed per day
    PEOPLE = 4
    CUPS_PER_PERSON = 2

    # Define the amount of coffee per cup and the cost per ounce of coffee
    COFFEE_PER_CUP = 0.5 # in ounces
    COST_PER_OUNCE = 1.25 # in dollars

    # Calculate the total amount of coffee consumed per day
    total_coffee_per_day = PEOPLE * CUPS_PER_PERSON * COFFEE_PER_CUP

    # Calculate the total amount of coffee consumed per week
    total_coffee_per_week = total_coffee_per_day * 7

    # Calculate the total cost of the coffee per week
    total_cost = total_coffee_per_week * COST_PER_OUNCE

    # Display the total cost of the coffee per week
    result = total_cost
    return result

print(solution())