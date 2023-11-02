def solution():
    """Nadia is learning to play the piano. She normally makes 3 mistakes per 40 notes and can play about 60 notes a minute. If she plays for 8 minutes how many mistakes will she make on average?"""
    notes_per_minute = 60
    notes_per_session = notes_per_minute * 8
    mistakes_per_session = (notes_per_session / 40) * 3
    average_mistakes_per_note = mistakes_per_session / notes_per_session
    result = average_mistakes_per_note
    return result

print(solution())