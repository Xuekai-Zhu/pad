def solution():
    """Christine is subbing aquafaba for egg whites in baking. Every 2 tablespoons of aquafaba is equivalent to 1 egg white. She's making 2 angel food cakes that call for 8 egg whites each. How many tablespoons of aquafaba will she need in order not to use egg whites?"""
    num_cakes = 2
    egg_whites_per_cake = 8
    tablespoons_per_egg_white = 2
    total_egg_whites = num_cakes * egg_whites_per_cake
    total_aquafaba = total_egg_whites * tablespoons_per_egg_white
    result = total_aquafaba
    return result

print(solution())