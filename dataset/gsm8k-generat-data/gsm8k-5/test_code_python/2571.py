def solution():
    chickens = 4  # Eric has 4 chickens
    eggs_per_chicken_per_day = 3  # Each chicken lays 3 eggs per day
    days = 3  # Eric collects the eggs after 3 days

    # Calculate the total number of eggs Eric will collect
    total_eggs = chickens * eggs_per_chicken_per_day * days
    result = total_eggs
    return result

print(solution())