def solution():
    # Calculate the time John spent exploring the jungle
    exploring_time = 3

    # Calculate the time John spent writing up notes about his travels
    notes_time = exploring_time / 2

    # Calculate the total time John spent on his book
    book_time = notes_time + 0.5

    # Calculate the total time John spent exploring and working on his book
    total_time = exploring_time + book_time
    result = total_time
    return result

print(solution())