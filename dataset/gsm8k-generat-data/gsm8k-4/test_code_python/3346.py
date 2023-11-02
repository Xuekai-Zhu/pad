def solution():
    """Susan had a sum of money. She spent 1/5 of it in September, 1/4 of it in October, and $120 in November. After spending these amounts of money, she still had $540 left. How much money did she have at first?"""
    # Define the remaining amount of money after November
    remaining_money = 540

    # Calculate the amount spent in November
    spent_money_november = 120

    # Define the fraction spent in September and October, respectively
    spent_fraction_september = 1/5
    spent_fraction_october = 1/4

    # Define the remaining fraction after September and October, respectively
    remaining_fraction_september = 1 - spent_fraction_september
    remaining_fraction_october = 1 - spent_fraction_october

    # Calculate the total amount of money spent
    total_spent = spent_money_november + remaining_money

    # Calculate the remaining amount of money after September and October
    remaining_money_october = remaining_fraction_october * (total_spent / remaining_fraction_september)
    remaining_money_september = remaining_fraction_september * (total_spent)

    # Calculate the initial amount of money
    initial_money = remaining_money + spent_money_november + remaining_money_october + remaining_money_september

    # Return the result
    result = initial_money
    return result

print(solution())