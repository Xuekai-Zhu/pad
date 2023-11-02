def solution():
    notes_per_minute = 60  # Nadia can play 60 notes per minute
    notes_per_hour = notes_per_minute * 60  # Nadia can play this many notes in an hour
    total_notes = notes_per_hour * 8  # Nadia plays for 8 minutes, so she plays this many notes in total
    mistakes_per_note = 3/40  # Nadia makes 3 mistakes per 40 notes
    total_mistakes = mistakes_per_note * total_notes  # Nadia makes this many mistakes in total

    # Calculate the average number of mistakes per minute
    average_mistakes = total_mistakes / 8
    result = average_mistakes
    return result

print(solution())