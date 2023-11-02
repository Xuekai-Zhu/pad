def solution():
    rate = 14  # The rate for mowing a lawn is $14 per hour
    hours_per_day = 2  # David mowed for 2 hours a day
    days_per_week = 7  # David mowed for a week

    # Calculate the total amount of money David made from mowing lawns
    total_money = rate * hours_per_day * days_per_week

    # Calculate the amount of money David spent on shoes
    money_spent_on_shoes = total_money / 2

    # Calculate the remaining money after buying the shoes
    remaining_money = total_money - money_spent_on_shoes

    # Calculate the amount of money David gave to his mom
    money_given_to_mom = remaining_money / 2

    # Calculate the total amount of money David has left
    total_money_left = remaining_money - money_given_to_mom

    result = total_money_left
    return result

print(solution())