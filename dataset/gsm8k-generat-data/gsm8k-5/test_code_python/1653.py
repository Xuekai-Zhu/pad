def solution():
    total_chapters = 8  # The book has 8 chapters
    chapters_read = 2  # Beth has already read 2 chapters
    remaining_chapters = total_chapters - chapters_read  # Beth needs to read the remaining chapters

    # Calculate Beth's reading rate in chapters per hour
    rate = chapters_read / 3  # Beth reads 2 chapters in 3 hours

    # Calculate the time required to finish reading the remaining chapters
    time_required = remaining_chapters / rate
    result = time_required
    return result

print(solution())