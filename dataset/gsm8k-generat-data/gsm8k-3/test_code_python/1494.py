def solution():
    """Micah has 7 fish in his aquarium. Kenneth has three times as many fish in his aquarium and Matthias has 15 less fish than Kenneth in his aquarium. How many fish do the boys have in total?"""
    # Define the number of fish for Micah, and calculate for Kenneth and Matthias
    micah_fish = 7
    kenneth_fish = micah_fish * 3
    matthias_fish = kenneth_fish - 15

    # Calculate the total number of fish
    total_fish = micah_fish + kenneth_fish + matthias_fish

    # Display the total number of fish
    result = total_fish
    return result

print(solution())