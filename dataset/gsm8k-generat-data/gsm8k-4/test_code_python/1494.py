def solution():
    """Micah has 7 fish in his aquarium. Kenneth has three times as many fish in his aquarium and Matthias has 15 less fish than Kenneth in his aquarium. How many fish do the boys have in total?"""
    # Define the number of fish in Micah's aquarium
    micah_fish = 7

    # Define the number of fish in Kenneth's aquarium
    kenneth_fish = micah_fish * 3

    # Define the number of fish in Matthias's aquarium
    matthias_fish = kenneth_fish - 15

    # Calculate the total number of fish
    total_fish = micah_fish + kenneth_fish + matthias_fish

    # Return the result
    result = total_fish
    return result

print(solution())