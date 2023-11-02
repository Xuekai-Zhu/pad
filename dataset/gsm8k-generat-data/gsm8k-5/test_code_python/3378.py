def solution():
    amount_earned = 120  # Krista sold $120 worth of eggs
    price_per_dozen = 3  # Krista sells eggs for $3 per dozen
    dozens_sold = amount_earned / price_per_dozen  # Calculate the number of dozens sold in 4 weeks
    total_eggs = dozens_sold * 12  # Calculate the total number of eggs sold in 4 weeks
    hens = 10  # Krista has 10 hens
    eggs_per_week_per_hen = total_eggs / (4 * hens)  # Calculate the number of eggs each hen lays per week
    result = eggs_per_week_per_hen
    return result

print(solution())