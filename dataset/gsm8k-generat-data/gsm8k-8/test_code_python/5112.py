def solution():
    # Calculate the number of smaller note papers from one folded and cut letter-size paper
    smaller_note_papers_per_folded_paper = 8

    # Calculate the total number of smaller note papers from 5 folded and cut letter-size papers
    total_smaller_note_papers = 5 * smaller_note_papers_per_folded_paper

    # Calculate the number of days one notepad would last if someone wrote 10 notes per day
    notes_per_day = 10
    notes_per_notepad = total_smaller_note_papers / notes_per_day
    result = notes_per_notepad
    return result

print(solution())