def solution():
    total_medals = 20
    track_medals = 5
    swimming_medals = track_medals * 2
    badminton_medals = total_medals - (track_medals + swimming_medals)
    result = badminton_medals
    return result

print(solution())