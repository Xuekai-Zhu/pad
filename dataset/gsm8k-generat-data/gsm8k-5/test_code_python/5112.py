def solution():
    paper_pieces = 5  # Alissa folds 5 pieces of paper at once
    folds = 3  # Alissa folds each piece of paper 3 times
    note_papers_per_piece = 8  # Alissa gets 8 small note papers from each folded piece of paper
    note_papers_per_notepad = paper_pieces * note_papers_per_piece  # Alissa combines the small note papers to form 1 notepad
    notes_per_day = 10  # Someone writes 10 notes per day
    days_per_notepad = note_papers_per_notepad / notes_per_day  # Calculate how long 1 notepad will last

    result = days_per_notepad
    return result

print(solution())