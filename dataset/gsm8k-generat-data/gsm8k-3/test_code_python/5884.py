def solution():
    """Jameson has 20 medals. Five of the medals are for the track. He has two times as many swimming medals as track medals. The rest of the medals are for badminton. How many badminton medals does he have?"""
    # Define the number of track medals and calculate the number of swimming medals
    track_medals = 5
    swimming_medals = 2 * track_medals

    # Calculate the total number of track and swimming medals
    total_track_swimming = track_medals + swimming_medals

    # Calculate the number of badminton medals
    badminton_medals = 20 - total_track_swimming

    # Display the number of badminton medals
    result = badminton_medals
    return result

print(solution())