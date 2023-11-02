def solution():
    """A farmer has 46 chickens. Each chicken gives him 6 eggs a week. If he sells a dozen eggs for $3, how much money would he make in 8 weeks?"""
    # Define the number of chickens and eggs per week
    num_chickens = 46
    eggs_per_chicken_per_week = 6

    # Calculate the total number of eggs produced in 8 weeks
    total_eggs = num_chickens * eggs_per_chicken_per_week * 8

    # Calculate the total number of dozens of eggs produced in 8 weeks
    total_dozens = total_eggs / 12

    # Calculate the total money made in 8 weeks
    total_money = total_dozens * 3

    result = total_money
    return result

print(solution())