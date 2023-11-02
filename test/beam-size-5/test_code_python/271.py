def solution():
    
    # Define the number of lines in the lyrics
    lyrics_lines = 54

    # Calculate the number of lines in the first scene
    first_scene_lines = 2 * lyrics_lines

    # Calculate the number of lines in the second scene
    second_scene_lines = song_lines + 6

    # Calculate the number of lines in the four-fifths of the lyrics
    four_fifths_lines = 4/5 * lyrics_lines

    # Calculate the total number of lines Sean has to memorize
    total_lines = lyrics_lines + first_scene_lines + second_scene_lines + four_fifths_lines

    # Display the total number of lines Sean has to memorize
    result = total_lines
    return result

print(solution())