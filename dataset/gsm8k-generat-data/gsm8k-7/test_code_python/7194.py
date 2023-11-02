def solution():
    julien_distance = 50

    # Calculate Sarah's distance
    sarah_distance = julien_distance * 2

    # Calculate Jamir's distance
    jamir_distance = sarah_distance + 20

    # Calculate the total distance they swim daily
    total_distance = julien_distance + sarah_distance + jamir_distance

    # Calculate the total distance they swim for the whole week (7 days)
    total_week_distance = total_distance * 7
    result = total_week_distance
    return result

print(solution())