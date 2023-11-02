def solution():
    # Calculate the total number of notes Nadia plays
    total_notes = 60 * 8

    # Calculate the total number of mistakes Nadia will make
    total_mistakes = (total_notes / 40) * 3

    # Calculate the average number of mistakes per minute
    avg_mistakes_per_minute = total_mistakes / 8

    result = avg_mistakes_per_minute
    return result

print(solution())