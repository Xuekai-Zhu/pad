def solution():
    """John spent 3 years of his life exploring the jungle. He then spent half as much time writing up notes about his travels. It took .5 years to write his book once he was done with the notes. How long did he spend on his book and exploring?"""
    years_exploring = 3
    years_writing = years_exploring / 2
    years_book = 0.5
    total_time = years_exploring + years_writing + years_book
    result = total_time
    return result

print(solution())