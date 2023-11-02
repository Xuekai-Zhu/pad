def solution():
    """Alissa used discarded paper to make notepads for her friends. She would fold 5 pieces of letter-size paper 3 times then cut along the edges to form smaller note papers. She would then stack these smaller note papers and staple them together. How long would 1 notepad last if someone wrote 10 notes per day?"""
    pieces_of_paper = 5
    folds_per_paper = 3
    notes_per_day = 10
    pages_per_paper = 2**folds_per_paper * pieces_of_paper
    notes_per_paper = pages_per_paper / 2
    days_per_paper = notes_per_paper / notes_per_day
    result = days_per_paper
    return result

print(solution())