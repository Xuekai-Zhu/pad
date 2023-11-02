def solution():
    """James needs 40 fish to make one sushi roll. He goes to the market and buys 400 fish, but later finds out that 20% of the fish have gone bad and cannot be used. How many sushi rolls did James make with the remaining fish?"""
    needed_fish_per_roll = 40
    total_fish = 400
    bad_fish_percentage = 0.2
    good_fish = (1 - bad_fish_percentage) * total_fish
    sushi_rolls = good_fish // needed_fish_per_roll
    result = sushi_rolls
    return result

print(solution())