def solution():
    """James needs 40 fish to make one sushi roll. He goes to the market and buys 400 fish, but later finds out that 20% of the fish have gone bad and cannot be used. How many sushi rolls did James make with the remaining fish?"""
    # Define the number of fish needed for one sushi roll
    FISH_PER_ROLL = 40

    # Define the total number of fish James bought
    total_fish = 400

    # Calculate the number of fish that cannot be used
    bad_fish = total_fish * 0.2

    # Calculate the number of fish that can be used
    good_fish = total_fish - bad_fish

    # Calculate the number of sushi rolls James can make
    sushi_rolls = good_fish / FISH_PER_ROLL

    # Display the number of sushi rolls James can make
    result = sushi_rolls
    return result

print(solution())