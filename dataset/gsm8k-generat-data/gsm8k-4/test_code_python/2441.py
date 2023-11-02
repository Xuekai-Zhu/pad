def solution():
    """There are 30 fish in the tank. One third of them are blue, and half of the blue fish have spots. How many fish in the tank are blue, spotted fish?"""
    # Define the total number of fish in the tank
    total_fish = 30

    # Calculate the number of blue fish
    blue_fish = total_fish // 3

    # Calculate the number of blue, spotted fish
    blue_spotted_fish = blue_fish // 2

    # Return the result
    result = blue_spotted_fish
    return result

print(solution())