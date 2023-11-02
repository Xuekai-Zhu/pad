def solution():
    """There are many fish in the tank. One third of them are blue, and half of the blue fish have spots. If there are 10 blue, spotted fish, how many fish are there in the tank?"""
    blue_spotted_fish = 10
    blue_fish = blue_spotted_fish * 2
    total_blue_fish = blue_fish * 3
    total_fish = total_blue_fish * 3
    result = total_fish
    return result

print(solution())