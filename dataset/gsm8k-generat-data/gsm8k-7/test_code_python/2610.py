def solution():
    num_chickens = 46
    eggs_per_week = 6
    num_weeks = 8
    eggs_per_dozen = 12
    price_per_dozen = 3

    # Calculate the total number of eggs produced in 8 weeks
    total_eggs = num_chickens * eggs_per_week * num_weeks

    # Calculate the total number of dozens of eggs produced
    total_dozen = total_eggs / eggs_per_dozen

    # Calculate the total revenue from selling the eggs
    total_revenue = total_dozen * price_per_dozen
    result = total_revenue
    return result

print(solution())