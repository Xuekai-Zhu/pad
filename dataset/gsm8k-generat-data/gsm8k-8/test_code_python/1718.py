def solution():
    # Calculate the number of fish caught by the kingfisher
    kingfisher_catch = 13 + 7

    # Calculate the total number of fish caught by both birds
    total_catch = 13 + kingfisher_catch

    # Calculate the number of fish caught by the fisherman
    fisherman_catch = 3 * total_catch

    # Calculate the difference in fish caught between the fisherman and the pelican
    difference = fisherman_catch - 13

    result = difference
    return result

print(solution())