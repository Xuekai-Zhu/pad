def solution():
    # Calculate the number of red notes
    num_red = 5 * 6

    # Calculate the number of blue notes under the red notes
    num_blue_under_red = 2 * num_red

    # Calculate the number of blue notes scattered at the bottom
    num_blue_scattered = 10

    # Add the number of red and blue notes to get the total number of notes retrieved
    total_notes = num_red + num_blue_under_red + num_blue_scattered

    # Divide the total number of notes in half to find the number of notes in each bin
    notes_per_bin = total_notes / 2

    result = notes_per_bin
    return result

print(solution())