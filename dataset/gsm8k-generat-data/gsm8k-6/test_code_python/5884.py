def solution():
    # Calculate the number of swimming medals
    track_medals = 5
    swimming_medals = 2 * track_medals

    # Calculate the number of badminton medals
    total_medals = 20
    badminton_medals = total_medals - track_medals - swimming_medals
    result = badminton_medals
    return result

print(solution())