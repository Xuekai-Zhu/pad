def solution():
    # Calculate the total number of notes played by Nadia
    total_notes = 60 * 8

    # Calculate the total number of mistakes Nadia will make
    total_mistakes = (total_notes / 40) * 3

    # Calculate the average number of mistakes made per minute
    average_mistakes = total_mistakes / 8

    result = average_mistakes
    return result

print(solution())