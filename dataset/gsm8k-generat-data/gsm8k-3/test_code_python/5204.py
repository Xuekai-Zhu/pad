def solution():
    """John spent 3 years of his life exploring the jungle.  He then spent half as much time writing up notes about his travels.  It took .5 years to write his book once he was done with the notes.  How long did he spend on his book and exploring?"""
    # Calculate the time spent exploring the jungle
    exploring_time = 3

    # Calculate the time spent writing up notes
    note_time = exploring_time / 2

    # Calculate the total time spent on the book
    book_time = note_time + 0.5

    # Calculate the total time spent exploring and working on the book
    total_time = exploring_time + book_time

    # Display the total time
    result = total_time
    return result

print(solution())