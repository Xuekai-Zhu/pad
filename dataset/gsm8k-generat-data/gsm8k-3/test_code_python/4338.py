def solution():
    """There are many fish in the tank. One third of them are blue, and half of the blue fish have spots. If there are 10 blue, spotted fish, how many fish are there in the tank?"""
    # Define the proportion of the blue fish and the spotted blue fish
    BLUE_PROPORTION = 1/3
    SPOTTED_BLUE_PROPORTION = 1/6

    # Define the number of blue spotted fish
    blue_spotted_fish = 10

    # Calculate the total number of blue fish
    blue_fish = blue_spotted_fish / SPOTTED_BLUE_PROPORTION

    # Calculate the total number of fish in the tank
    total_fish = blue_fish / BLUE_PROPORTION

    # Display the total number of fish in the tank
    result = total_fish
    return result

print(solution())