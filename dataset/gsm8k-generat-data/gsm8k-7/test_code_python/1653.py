def solution():
    total_chapters = 8
    chapters_read = 2
    hours_per_chapter = 3

    # Calculate the total number of remaining chapters
    remaining_chapters = total_chapters - chapters_read

    # Calculate the total number of hours needed to complete the remaining chapters
    total_hours = remaining_chapters * hours_per_chapter
    result = total_hours
    return result

print(solution())