def solution():
    # Calculate the total amount of money Carl earns in 4 weeks
    candy_money = 0.50
    trash_money = 0.75 * 4
    total_money = candy_money * (trash_money / candy_money)

    # Calculate the number of candy bars Carl can buy with the total amount of money earned
    candy_bars = total_money / candy_money
    result = candy_bars
    return result

print(solution())