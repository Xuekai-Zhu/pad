def solution():
    """James needs 40 fish to make one sushi roll. He goes to the market and buys 400 fish, but later finds out that 20% of the fish have gone bad and cannot be used. How many sushi rolls did James make with the remaining fish?"""
    # Define the number of fish needed for one sushi roll and the initial number of fish bought
    FISH_PER_ROLL = 40
    INITIAL_FISH = 400

    # Calculate the number of fish that went bad
    bad_fish = INITIAL_FISH * 0.2

    # Calculate the number of usable fish remaining
    remaining_fish = INITIAL_FISH - bad_fish

    # Calculate the number of sushi rolls that can be made with the remaining fish
    sushi_rolls = remaining_fish // FISH_PER_ROLL

    # return the result
    result = sushi_rolls
    return result

print(solution())