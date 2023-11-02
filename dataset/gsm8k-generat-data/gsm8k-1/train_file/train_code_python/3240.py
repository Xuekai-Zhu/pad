def solution():
    """James needs 40 fish to make one sushi roll. He goes to the market and buys 400 fish, but later finds out that 20% of the fish have gone bad and cannot be used. How many sushi rolls did James make with the remaining fish?"""
    fish_per_roll = 40
    total_fish = 400
    bad_fish_percent = 20
    bad_fish = total_fish * (bad_fish_percent / 100)
    good_fish = total_fish - bad_fish
    sushi_rolls = good_fish // fish_per_roll
    result = sushi_rolls
    return result

print(solution())