def solution():
    """Jake is retrieving the notes on a communal board, putting all of the red notes in the complaints bin and all of the blue notes in the compliments bin. The red notes were in 5 rows with 6 notes in each row. There are 2 blue notes under each of the red notes, as well as another 10 blue notes scattered at the bottom of the board. How many notes in total are put into the complaints and compliments bins?"""
    # Calculate the total number of red notes
    red_notes = 5 * 6

    # Calculate the total number of blue notes under the red notes
    blue_notes_under_red = red_notes * 2

    # Calculate the total number of blue notes at the bottom of the board
    blue_notes_bottom = 10

    # Calculate the total number of notes put into the complaints bin
    complaints = red_notes

    # Calculate the total number of notes put into the compliments bin
    compliments = blue_notes_under_red + blue_notes_bottom

    # Calculate the total number of notes
    total_notes = complaints + compliments

    # return the result
    result = total_notes
    return result

print(solution())