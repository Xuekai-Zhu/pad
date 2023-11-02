def solution():
    marbles_per_bag = 28 // 4
    remaining_bags = 4 - 1
    remaining_marbles = marbles_per_bag * remaining_bags
    result = remaining_marbles
    return result

print(solution())