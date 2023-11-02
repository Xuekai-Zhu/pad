def solution():
    red_notes = 5 * 6  # number of red notes
    blue_notes_under_red = 2 * red_notes  # number of blue notes under red notes
    blue_notes_at_bottom = 10  # number of blue notes at the bottom of the board
    total_notes = red_notes + blue_notes_under_red + blue_notes_at_bottom

    # Separate the red and blue notes and calculate the final number of notes in each bin
    complaints = red_notes
    compliments = blue_notes_under_red + blue_notes_at_bottom
    result = (complaints, compliments)
    return result

print(solution())