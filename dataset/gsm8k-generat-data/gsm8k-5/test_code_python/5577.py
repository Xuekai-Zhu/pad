def solution():
    servings_24oz = 60  # 24oz barrel has 60 servings
    cheeseballs_serving = 12  # Each serving has 12 cheese balls
    oz_35 = 35  # 35oz barrel

    # Calculate the total cheese balls in a 24oz barrel
    total_cheeseballs_24oz = servings_24oz * cheeseballs_serving

    # Calculate the cheese balls per ounce in a 24oz barrel
    cheeseballs_per_oz_24oz = total_cheeseballs_24oz / 24

    # Calculate the total cheese balls in a 35oz barrel
    total_cheeseballs_35oz = oz_35 * cheeseballs_per_oz_24oz
    result = total_cheeseballs_35oz
    return result

print(solution())