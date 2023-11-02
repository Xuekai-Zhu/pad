def solution():
    """The rate for mowing a lawn is $14 per hour. David mowed for 2 hours a day for a week. He then spent half of the money he made from mowing a lawn on a pair of shoes and gave half of the remaining money to his mom. How much money did he have left?"""
    # Define the rate for mowing a lawn
    RATE = 14

    # Calculate the total hours mowed for a week
    hours_mowed = 2 * 7

    # Calculate the total money earned
    total_money = hours_mowed * RATE

    # Calculate the amount spent on shoes
    shoes_cost = total_money / 2

    # Calculate the remaining money
    remaining_money = total_money - shoes_cost

    # Calculate the amount given to his mom
    mom_money = remaining_money / 2

    # Calculate the final amount David has left
    final_money = remaining_money - mom_money

    result = final_money
    return result

print(solution())