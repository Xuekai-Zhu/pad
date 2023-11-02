def solution():
    pelican_fish = 13  # The pelican caught 13 fish
    kingfisher_fish = pelican_fish + 7  # The kingfisher caught 7 more fish than the pelican
    total_fish = pelican_fish + kingfisher_fish  # The total amount of fish caught by the pelican and kingfisher
    fisherman_fish = 3 * total_fish  # The fisherman caught 3 times the total amount of fish caught by the pelican and kingfisher

    # Calculate the difference in the number of fish caught by the fisherman and the pelican
    diff_fish = fisherman_fish - pelican_fish
    result = diff_fish
    return result

print(solution())