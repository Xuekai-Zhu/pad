def solution():
    """Nadia is learning to play the piano. She normally makes 3 mistakes per 40 notes and can play about 60 notes a minute. If she plays for 8 minutes how many mistakes will she make on average?"""
    notes_per_minute = 60
    notes_played = notes_per_minute * 8
    mistakes_per_note = 3 / 40
    total_mistakes = notes_played * mistakes_per_note
    result = total_mistakes
    return result

print(solution())