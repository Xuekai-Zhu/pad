def solution():
    num_rows = 5
    notes_per_row = 6
    num_red_notes = num_rows * notes_per_row
    num_blue_notes_under_red = 2 * num_red_notes
    num_scattered_blue_notes = 10

    # Calculate the total number of red notes in the complaints bin
    num_red_notes_in_complaints = num_red_notes

    # Calculate the total number of blue notes in the compliments bin
    num_blue_notes_in_compliments = num_blue_notes_under_red + num_scattered_blue_notes

    # Calculate the total number of notes in both bins
    total_notes = num_red_notes_in_complaints + num_blue_notes_in_compliments
    result = total_notes
    return result

print(solution())