def solution():
    # Calculate the total amount of money earned in a week
    total_hours = 2 * 7
    total_earned = total_hours * 14

    # Calculate the amount spent on shoes
    shoes_cost = total_earned / 2

    # Calculate the amount left after buying shoes
    remaining_money = total_earned - shoes_cost

    # Calculate the amount given to his mom
    mom_money = remaining_money / 2

    # Calculate the final amount left
    final_money = remaining_money - mom_money
    result = final_money
    return result

print(solution())