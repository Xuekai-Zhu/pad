def solution():
    # Calculate the total number of small note papers from 1 letter-size paper
    small_note_papers = 2**3 * 2**3 * 2**3 * 5  # 5 pieces of letter-size paper folded 3 times each, total 2**3 * 2**3 * 2**3 small note papers

    # Calculate the total number of notes that can be written on 1 notepad
    notes_per_notepad = small_note_papers * 10  # 10 notes can be written on each small note paper

    # Calculate how long 1 notepad would last if someone wrote 10 notes per day
    notepad_lasting_days = notes_per_notepad / 10  # 1 notepad lasts as long as the number of notes on it, divided by the number of notes written per day
    result = notepad_lasting_days
    return result

print(solution())