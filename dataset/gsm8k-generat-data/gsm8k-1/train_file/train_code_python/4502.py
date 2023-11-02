def solution():
    """Christine is subbing aquafaba for egg whites in baking. Every 2 tablespoons of aquafaba is equivalent to 1 egg white. She's making 2 angel food cakes that call for 8 egg whites each. How many tablespoons of aquafaba will she need in order not to use egg whites?"""
    egg_whites_per_cake = 8
    aquafaba_per_egg_white = 2
    total_aquafaba_needed = egg_whites_per_cake * 2 * aquafaba_per_egg_white
    result = total_aquafaba_needed
    return result

print(solution())