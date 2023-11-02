def solution():
    egg_whites_per_cake = 8  # Each cake calls for 8 egg whites
    tablespoons_per_egg_white = 2  # 2 tablespoons of aquafaba is equivalent to 1 egg white
    total_eggs_needed = egg_whites_per_cake * 2  # Christine is making 2 cakes
    total_tablespoons_needed = total_eggs_needed * tablespoons_per_egg_white  # Convert egg whites to tablespoons of aquafaba
    result = total_tablespoons_needed
    return result

print(solution())