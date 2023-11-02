def solution():
    """Bobby has an aquarium with twice as many fish as Sarah's has. Sarah has 5 more fish in her aquarium than Tony does. Tony has 3 times as many fish in his aquarium as Billy does. Billy has 10 fish. How many fish do all 4 people have put together?"""
    bobby_fish = 2 * (5 + 3 * 10)
    sarah_fish = 5 + 3 * 10
    tony_fish = 3 * 10
    billy_fish = 10
    total_fish = bobby_fish + sarah_fish + tony_fish + billy_fish
    result = total_fish
    return result

print(solution())