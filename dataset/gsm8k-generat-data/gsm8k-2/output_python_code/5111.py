def solution():
    """Alissa used discarded paper to make notepads for her friends. She would fold 5 pieces of letter-size paper 3 times then cut along the edges to form smaller note papers. She would then stack these smaller note papers and staple them together. How long would 1 notepad last if someone wrote 10 notes per day?"""
    letter_size_paper = 5
    num_folds = 3
    num_note_pages = (letter_size_paper * (2 ** num_folds)) / 2
    num_notes_per_day = 10
    num_days = num_note_pages / num_notes_per_day
    result = num_days
    return result

print(solution())