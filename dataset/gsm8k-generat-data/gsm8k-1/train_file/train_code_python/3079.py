def solution():
    """Tony has two fish. Every year, his parents buy him two more, but one of them dies. How many fish will he have in five years?"""
    initial_fish = 2
    fish_per_year = 2
    years = 5
    total_fish = initial_fish
    for i in range(years):
        total_fish += (fish_per_year - 1)
    result = total_fish
    return result

print(solution())