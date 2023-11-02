def solution():
    """Nadia is learning to play the piano. She normally makes 3 mistakes per 40 notes and can play about 60 notes a minute. If she plays for 8 minutes how many mistakes will she make on average?"""
    # Define the number of notes played in 8 minutes
    notes_played = 60 * 8

    # Calculate the number of mistakes per note
    mistakes_per_note = 3 / 40

    # Calculate the total number of mistakes made
    total_mistakes = notes_played * mistakes_per_note

    # return the result
    result = total_mistakes
    return result

print(solution())