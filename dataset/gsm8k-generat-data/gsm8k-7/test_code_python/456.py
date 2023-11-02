def solution():
    money_from_mowing = 600
    money_from_gifts = 250
    money_from_selling_games = 150
    money_from_odd_jobs = 150

    total_money = money_from_mowing + money_from_gifts + money_from_selling_games + money_from_odd_jobs

    percentage_to_save = 0.4

    savings = total_money * percentage_to_save
    result = savings
    return result

print(solution())