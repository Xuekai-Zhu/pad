def solution():
    """John spent 3 years of his life exploring the jungle. He then spent half as much time writing up notes about his travels. It took .5 years to write his book once he was done with the notes. How long did he spend on his book and exploring?"""
    exploring_time = 3
    note_taking_time = exploring_time / 2
    book_writing_time = note_taking_time + 0.5
    total_time = exploring_time + book_writing_time
    result = total_time
    return result

print(solution())