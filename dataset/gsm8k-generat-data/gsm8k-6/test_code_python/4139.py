def solution():
    # Calculate the total number of ninja throwing stars
    chad_stars = 4 * 2  # Chad has twice as many as Eric
    chad_stars -= 2  # Jeff bought 2 stars from Chad
    total_stars = chad_stars + 6  # Jeff now has 6 stars
    result = total_stars
    return result

print(solution())