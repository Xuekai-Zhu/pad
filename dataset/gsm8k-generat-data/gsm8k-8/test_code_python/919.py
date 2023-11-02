def solution():
    # Calculate the total number of songs Aisha had after adding the first 500
    total_songs = 500 + 500

    # Calculate the number of songs Aisha added the following week
    added_songs = 2 * total_songs

    # Calculate the total number of songs Aisha had after adding the second batch of songs
    total_songs += added_songs

    # Remove the 50 songs Aisha didn't like
    total_songs -= 50

    result = total_songs
    return result

print(solution())