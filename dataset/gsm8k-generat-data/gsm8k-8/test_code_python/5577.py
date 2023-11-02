def solution():
    # Calculate the total number of servings in the 24oz barrel
    servings_24oz = 60

    # Calculate the total number of cheese balls in the 24oz barrel
    cheeseballs_24oz = servings_24oz * 12

    # Calculate the ratio of cheese balls to ounces in the 24oz barrel
    ratio_24oz = cheeseballs_24oz / 24

    # Use the ratio to calculate the number of cheese balls in the 35oz barrel
    cheeseballs_35oz = ratio_24oz * 35

    result = cheeseballs_35oz
    return result

print(solution())