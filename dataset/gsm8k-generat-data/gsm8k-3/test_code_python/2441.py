def solution():
    """There are 30 fish in the tank. One third of them are blue, and half of the blue fish have spots. How many fish in the tank are blue, spotted fish?"""
    # Define the number of fish in the tank
    total_fish = 30

    # Calculate the number of blue fish
    blue_fish = total_fish // 3

    # Calculate the number of blue fish with spots
    spotted_fish = blue_fish // 2

    # Display the number of blue, spotted fish
    result = spotted_fish
    return result

print(solution())