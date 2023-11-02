def solution():
    eggs_per_chicken_per_week = 6  # Each chicken lays 6 eggs per week
    total_eggs_per_week = 10 * eggs_per_chicken_per_week  # There are 10 chickens
    dozens_of_eggs_per_week = total_eggs_per_week / 12  # Convert to dozens of eggs
    price_per_dozen = 2  # Jane can sell the eggs for $2/dozen

    # Calculate the total money Jane will make in 2 weeks
    total_money = dozens_of_eggs_per_week * price_per_dozen * 2  # 2 weeks

    result = total_money
    return result

print(solution())