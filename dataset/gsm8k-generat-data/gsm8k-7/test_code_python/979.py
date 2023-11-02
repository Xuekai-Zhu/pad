def solution():
    parker_distance = 16
    grant_distance = parker_distance * 1.25
    kyle_distance = grant_distance * 2

    # Calculate the difference in distance between Parker and Kyle
    diff_distance = kyle_distance - parker_distance

    result = diff_distance
    return result

print(solution())