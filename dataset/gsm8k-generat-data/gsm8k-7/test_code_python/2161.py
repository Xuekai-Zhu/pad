def solution():
    initial_money = 10
    donation = 4
    charity_prize = 90
    lost_at_casino = 50 + 10 + 5
    water_bottle = 1
    lottery_ticket = 1
    lottery_prize = 65

    # Calculate Renata's total expenses
    total_expenses = donation + lost_at_casino + water_bottle + lottery_ticket

    # Calculate Renata's total winnings
    total_winnings = charity_prize + lottery_prize

    # Calculate the total amount of money that Renata has
    total_money = initial_money + total_winnings - total_expenses
    result = total_money
    return result

print(solution())