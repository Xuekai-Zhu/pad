def solution():
    """Tony has two fish. Every year, his parents buy him two more, but one of them dies. How many fish will he have in five years?"""
    num_fish = 2
    for i in range(5):
        num_fish += 1 # Buy 2 new fish, one dies
    result = num_fish
    return result

print(solution())