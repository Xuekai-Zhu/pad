def solution():
    # Calculate the number of fish caught by the kingfisher
    kingfisher_fish = 13 + 7  # the kingfisher caught 7 more fish than the pelican
    total_fish = 13 + kingfisher_fish  # the total number of fish caught by both birds
    fisherman_fish = 3 * total_fish  # the number of fish caught by the fisherman
    pelican_fish = 13  # the number of fish caught by the pelican

    # Calculate the difference between the number of fish caught by the fisherman and the pelican
    difference = fisherman_fish - pelican_fish
    result = difference
    return result

print(solution())