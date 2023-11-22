def solution():
    
    # Define the number of lines in the lyrics
    lyrics_lines = 54

    # Calculate the number of lines in the first scene
    first_scene_lines = lyrics_lines * 2

    # Calculate the number of lines in the second scene
    second_scene_lines = lyrics_lines + 6 + (lyrics_lines * 4/5)

    # Calculate the total number of lines
    total_lines = first_scene_lines + second_scene_lines

    # Display the total number of lines
    result = total_lines
    return result

print(solution())