def solution():
    """A pelican caught 13 fish and a kingfisher caught 7 more fish than the pelican. If a fisherman caught 3 times the total amount of fish the pelican and kingfisher caught, how many more fish did the fisherman catch than the pelican?"""
    # Define the number of fish caught by the pelican
    pelican_fish = 13

    # Calculate the number of fish caught by the kingfisher
    kingfisher_fish = pelican_fish + 7

    # Calculate the total number of fish caught by the pelican and kingfisher
    total_fish = pelican_fish + kingfisher_fish

    # Calculate the number of fish caught by the fisherman
    fisherman_fish = total_fish * 3

    # Calculate the difference between the number of fish caught by the fisherman and the pelican
    difference = fisherman_fish - pelican_fish

    # Return the result
    result = difference
    return result

print(solution())