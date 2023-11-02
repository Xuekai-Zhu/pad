def solution():
    """Alissa used discarded paper to make notepads for her friends. She would fold 5 pieces of letter-size paper 3 times then cut along the edges to form smaller note papers. She would then stack these smaller note papers and staple them together. How long would 1 notepad last if someone wrote 10 notes per day?"""
    # Define the number of small note papers from one piece of folded paper
    NOTE_PAPERS_PER_FOLDED_PAPER = 8

    # Define the number of small note papers from 5 pieces of letter-size paper
    NOTE_PAPERS_PER_NOTEPAD = NOTE_PAPERS_PER_FOLDED_PAPER * 5 * 2 * 2

    # Calculate the number of days one notepad lasts
    notes_per_day = 10
    notes_per_notepad = NOTE_PAPERS_PER_NOTEPAD * 2 # assume each note paper has 2 usable sides
    days_per_notepad = notes_per_notepad / notes_per_day

    # Display the number of days one notepad lasts
    result = days_per_notepad
    return result

print(solution())