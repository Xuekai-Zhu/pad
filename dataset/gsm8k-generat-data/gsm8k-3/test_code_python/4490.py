def solution():
    """Nadia is learning to play the piano. She normally makes 3 mistakes per 40 notes and can play about 60 notes a minute.   If she plays for 8 minutes how many mistakes will she make on average?"""
    # Define the number of notes per minute and mistakes per 40 notes
    NOTES_PER_MINUTE = 60
    MISTAKES_PER_40_NOTES = 3

    # Calculate the total number of notes played
    total_notes = NOTES_PER_MINUTE * 8

    # Calculate the number of mistakes made
    mistakes = (total_notes / 40) * MISTAKES_PER_40_NOTES

    # Display the average number of mistakes
    result = mistakes
    return result

print(solution())