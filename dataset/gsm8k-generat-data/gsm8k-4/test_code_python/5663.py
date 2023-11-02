def solution():
    """The rate for mowing a lawn is $14 per hour. David mowed for 2 hours a day for a week. He then spent half of the money he made from mowing a lawn on a pair of shoes and gave half of the remaining money to his mom. How much money did he have left?"""
    # Calculate the total number of hours David mowed
    total_hours = 2 * 7

    # Calculate the total amount of money David earned
    total_earned = total_hours * 14

    # Calculate the amount of money David spent on shoes
    shoes_cost = total_earned / 2

    # Calculate the amount of money David had left after buying shoes
    remaining_money = total_earned - shoes_cost

    # Calculate the amount of money David gave to his mom
    mom_money = remaining_money / 2

    # calculate the final amount of money David had left
    final_money = remaining_money - mom_money

    # Return the result
    result = final_money
    return result

print(solution())