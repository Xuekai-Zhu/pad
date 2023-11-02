def solution():
    """Olga has an aquarium with fish in 5 different colors. There are 12 yellow ones, half as many blue ones, and twice as many green ones as yellow ones. How many fish does Olga have in her aquarium?"""
    # Define the number of yellow fish
    yellow_fish = 12

    # Calculate the number of blue fish
    blue_fish = yellow_fish / 2

    # Calculate the number of green fish
    green_fish = yellow_fish * 2

    # Calculate the total number of fish
    total_fish = yellow_fish + blue_fish + green_fish

    # return the result
    result = total_fish
    return result

print(solution())