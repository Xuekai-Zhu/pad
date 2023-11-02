def solution():
    """Jameson has 20 medals. Five of the medals are for the track. He has two times as many swimming medals as track medals. The rest of the medals are for badminton. How many badminton medals does he have?"""
    # Define the number of medals Jameson has for track
    track_medals = 5

    # Define the number of swimming medals Jameson has
    swimming_medals = 2 * track_medals

    # Define the total number of medals Jameson has
    total_medals = 20

    # Calculate the number of badminton medals Jameson has
    badminton_medals = total_medals - track_medals - swimming_medals

    # Return the result
    result = badminton_medals
    return result

print(solution())