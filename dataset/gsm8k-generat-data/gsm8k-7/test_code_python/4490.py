def solution():
    mistakes_per_40_notes = 3
    notes_per_minute = 60
    time_in_minutes = 8

    # Calculate the total number of notes played
    total_notes = notes_per_minute * time_in_minutes

    # Calculate the number of times 40 notes are played
    num_40_note_sets = total_notes // 40

    # Calculate the total number of mistakes made
    total_mistakes = num_40_note_sets * mistakes_per_40_notes

    # Calculate the number of leftover notes after completing 40 note sets
    leftover_notes = total_notes % 40

    # Calculate the number of mistakes made on leftover notes
    mistakes_on_leftover_notes = round(leftover_notes * (mistakes_per_40_notes / 40))

    # Calculate the final average number of mistakes
    average_mistakes = (total_mistakes + mistakes_on_leftover_notes) / time_in_minutes

    result = average_mistakes
    return result

print(solution())