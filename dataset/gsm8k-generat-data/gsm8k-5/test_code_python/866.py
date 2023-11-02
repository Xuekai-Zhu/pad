def solution():
    # Calculate the number of red notes
    num_red_notes = 5 * 6  # 5 rows with 6 notes in each row

    # Calculate the number of blue notes under the red notes
    num_blue_notes_under_red = 2 * num_red_notes

    # Calculate the number of blue notes at the bottom of the board
    num_blue_notes_bottom = 10

    # Calculate the total number of notes put in the complaints bin
    num_complaints = num_red_notes

    # Calculate the total number of notes put in the compliments bin
    num_compliments = num_blue_notes_under_red + num_blue_notes_bottom

    # Calculate the total number of notes retrieved
    total_notes = num_complaints + num_compliments
    result = total_notes
    return result

print(solution())