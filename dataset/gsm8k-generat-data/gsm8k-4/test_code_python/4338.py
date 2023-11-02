def solution():
    """There are many fish in the tank. One third of them are blue, and half of the blue fish have spots. If there are 10 blue, spotted fish, how many fish are there in the tank?"""
    # Define the number of blue fish and blue, spotted fish
    blue_fish = 10
    blue_spotted_fish = blue_fish / 2

    # Calculate the total number of fish in the tank
    total_fish = (blue_spotted_fish * 3) * 2 

    result = total_fish
    return result

print(solution())