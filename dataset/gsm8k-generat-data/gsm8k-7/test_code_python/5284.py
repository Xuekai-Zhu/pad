def solution():
    num_chickens = 8
    eggs_per_chicken_per_day = 3
    days_per_week = 7
    weeks = 4
    dozen_price = 5

    # Calculate the total number of eggs that Kelly's chickens will lay in 4 weeks
    total_eggs = num_chickens * eggs_per_chicken_per_day * days_per_week * weeks

    # Calculate the total number of dozens of eggs
    total_dozens = total_eggs / 12

    # Calculate the total amount of money earned from selling all the eggs
    total_money = total_dozens * dozen_price
    result = total_money
    return result

print(solution())