def solution():
    # Define the number of songs played by Vivian and Clara
    vivian_songs = 10
    clara_songs = vivian_songs - 2

    # Calculate the number of weekdays in June
    weekdays = 30 - 8

    # Calculate the total number of songs played by both of them in June
    total_songs = (vivian_songs + clara_songs) * weekdays

    result = total_songs
    return result

print(solution())