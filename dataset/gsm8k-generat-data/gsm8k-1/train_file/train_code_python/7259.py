def solution():
    """A wildlife team is monitoring the number of birds in a park. There are 3 blackbirds in each of the park’s 7 trees. There are also 13 magpies roaming around the park. How many birds are in the park in total?"""
    blackbirds_per_tree = 3
    trees_in_park = 7
    magpies_in_park = 13
    total_blackbirds = blackbirds_per_tree * trees_in_park
    total_birds = total_blackbirds + magpies_in_park
    result = total_birds
    return result

print(solution())