def solution():
    num_chickens = 10
    eggs_per_chicken_per_week = 6
    eggs_per_dozen = 12
    price_per_dozen = 2
    num_weeks = 2
    
    # Calculate the total number of eggs produced in 2 weeks
    total_eggs = num_chickens * eggs_per_chicken_per_week * num_weeks
    
    # Calculate the total number of dozens of eggs produced in 2 weeks
    total_dozen = total_eggs / eggs_per_dozen
    
    # Calculate the total amount of money made from selling all the eggs
    total_money = total_dozen * price_per_dozen
    result = total_money
    return result

print(solution())