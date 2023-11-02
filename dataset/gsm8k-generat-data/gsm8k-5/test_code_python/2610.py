def solution():
    chickens = 46  # The farmer has 46 chickens
    eggs_per_chicken_per_week = 6  # Each chicken gives the farmer 6 eggs per week
    total_eggs = chickens * eggs_per_chicken_per_week * 8  # The total number of eggs after 8 weeks
    dozens_of_eggs = total_eggs / 12  # The total number of dozens of eggs
    price_per_dozen = 3  # The price of a dozen eggs is $3

    # Calculate the total amount of money the farmer would make in 8 weeks
    total_money = dozens_of_eggs * price_per_dozen
    result = total_money
    return result

print(solution())