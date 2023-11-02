def solution():
    parker_distance = 16
    grant_distance = parker_distance * 1.25
    kyle_distance = grant_distance * 2

    # Calculate how much farther Kyle threw the ball compared to Parker
    farther_distance = kyle_distance - parker_distance
    result = farther_distance
    return result

print(solution())