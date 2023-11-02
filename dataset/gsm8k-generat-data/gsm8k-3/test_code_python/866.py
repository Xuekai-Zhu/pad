def solution():
    """Jake is retrieving the notes on a communal board, putting all of the red notes in the complaints bin and all of the blue notes in the compliments bin. The red notes were in 5 rows with 6 notes in each row. There are 2 blue notes under each of the red notes, as well as another 10 blue notes scattered at the bottom of the board. How many notes in total are put into the complaints and compliments bins?"""
    # Calculate the number of red notes
    red_notes = 5 * 6

    # Calculate the number of blue notes under each red note
    blue_under_red = 2 * red_notes

    # Calculate the total number of blue notes
    total_blue = blue_under_red + 10

    # Put all red notes into complaints bin and all blue notes into compliments bin
    complaints = red_notes
    compliments = total_blue

    # Calculate the total number of notes
    total_notes = complaints + compliments

    # Display the total number of notes in complaints and compliments bins
    result = total_notes
    return result

print(solution())