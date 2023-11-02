def solution():
    """Jake is retrieving the notes on a communal board, putting all of the red notes in the complaints bin and all of the blue notes in the compliments bin. The red notes were in 5 rows with 6 notes in each row. There are 2 blue notes under each of the red notes, as well as another 10 blue notes scattered at the bottom of the board. How many notes in total are put into the complaints and compliments bins?"""
    red_notes = 5 * 6
    blue_notes_under_red = red_notes * 2
    blue_notes_scattered = 10
    total_notes = red_notes + blue_notes_under_red + blue_notes_scattered
    complaints_bin = red_notes
    compliments_bin = blue_notes_under_red + blue_notes_scattered
    result = (complaints_bin, compliments_bin)
    return result

print(solution())