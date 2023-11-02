def solution():
    chickens = 8  # Kelly has 8 chickens
    eggs_per_chicken_per_day = 3  # Each chicken lays 3 eggs per day
    eggs_per_day = chickens * eggs_per_chicken_per_day  # Total number of eggs per day
    dozens_per_day = eggs_per_day / 12  # Total number of dozens per day
    price_per_dozen = 5  # Kelly sells the eggs for $5 per dozen
    days_in_week = 7  # There are 7 days in a week
    weeks = 4  # Kelly wants to know how much money she will make in 4 weeks

    # Calculate the total number of dozens of eggs Kelly will sell in 4 weeks
    total_dozens = dozens_per_day * days_in_week * weeks

    # Calculate the total money Kelly will make in 4 weeks
    total_money = total_dozens * price_per_dozen
    result = total_money
    return result

print(solution())