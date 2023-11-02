def solution():
    
    notes_per_minute = 60
    notes_played = notes_per_minute * 8
    mistakes_per_note = 3 / 40
    total_mistakes = notes_played * mistakes_per_note
    result = total_mistakes
    return result

print(solution())