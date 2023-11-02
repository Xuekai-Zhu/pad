def solution():
    julien_swim_distance = 50
    sarah_swim_distance = julien_swim_distance * 2
    jamir_swim_distance = sarah_swim_distance + 20

    # Calculate the total swim distance for each person for the whole week
    weekly_julien_swim_distance = julien_swim_distance * 7
    weekly_sarah_swim_distance = sarah_swim_distance * 7
    weekly_jamir_swim_distance = jamir_swim_distance * 7

    # Calculate the combined swim distance for the whole week
    total_weekly_swim_distance = weekly_julien_swim_distance + weekly_sarah_swim_distance + weekly_jamir_swim_distance
    result = total_weekly_swim_distance
    return result

print(solution())