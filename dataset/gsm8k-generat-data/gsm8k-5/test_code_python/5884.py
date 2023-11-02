def solution():
    track_medals = 5  # Jameson has 5 track medals
    swimming_medals = 2 * track_medals  # Jameson has 2 times as many swimming medals as track medals
    total_medals = 20  # Jameson has 20 medals in total
    badminton_medals = total_medals - track_medals - swimming_medals  # Calculate the number of badminton medals

    result = badminton_medals
    return result

print(solution())