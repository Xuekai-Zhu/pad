def solution():
    """Alissa used discarded paper to make notepads for her friends. She would fold 5 pieces of letter-size paper 3 times then cut along the edges to form smaller note papers. She would then stack these smaller note papers and staple them together. How long would 1 notepad last if someone wrote 10 notes per day?"""
    # Define the number of letter-size papers used for each notepad
    num_papers = 5

    # Calculate the number of smaller note papers produced from folding and cutting each letter-size paper
    num_notes_per_paper = 2**3

    # Calculate the total number of smaller note papers produced for each notepad
    total_notes_per_notepad = num_papers * num_notes_per_paper

    # Calculate the number of days 1 notepad would last if someone wrote 10 notes per day
    days_per_notepad = total_notes_per_notepad / 10

    result = days_per_notepad
    return result

print(solution())