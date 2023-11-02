def solution():
    # Calculate the total amount of money David made from mowing lawns
    money_made = 14 * 2 * 7  # $14 per hour, 2 hours a day, for a week

    # Calculate the amount of money David spent on shoes
    shoes_cost = money_made / 2

    # Calculate the amount of money David gave to his mom
    remaining_money = money_made - shoes_cost
    mom_money = remaining_money / 2

    # Calculate the amount of money David had left
    money_left = remaining_money - mom_money
    result = money_left
    return result

print(solution())