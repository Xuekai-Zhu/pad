def solution():
    egg_whites_per_cake = 8
    tablespoons_per_egg_white = 2
    num_cakes = 2

    # Calculate the total number of egg whites needed
    total_egg_whites = egg_whites_per_cake * num_cakes

    # Calculate the total number of tablespoons of aquafaba needed
    total_aquafaba = total_egg_whites * tablespoons_per_egg_white

    result = total_aquafaba
    return result

print(solution())