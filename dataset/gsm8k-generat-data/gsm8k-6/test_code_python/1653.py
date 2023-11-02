def solution():
    # Calculate how many chapters Beth can read in 1 hour
    chapters_per_hour = 2 / 3  # Beth can read 2 chapters in 3 hours

    # Calculate how many hours it will take to finish reading the remaining chapters
    remaining_chapters = 8 - 2  # Beth has read 2 chapters out of 8
    hours_to_finish = remaining_chapters / chapters_per_hour

    result = hours_to_finish
    return result

print(solution())