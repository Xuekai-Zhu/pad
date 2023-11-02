def solution():
    """A pelican caught 13 fish and a kingfisher caught 7 more fish than the pelican. If a fisherman caught 3 times the total amount of fish the pelican and kingfisher caught, how many more fish did the fisherman catch than the pelican?"""
    pelican_fish = 13
    kingfisher_fish = pelican_fish + 7
    total_fish = pelican_fish + kingfisher_fish
    fisherman_fish = 3 * total_fish
    difference = fisherman_fish - pelican_fish
    result = difference
    return result

print(solution())