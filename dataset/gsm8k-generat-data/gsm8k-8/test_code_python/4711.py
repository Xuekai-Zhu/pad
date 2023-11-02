def solution():
    # Define the total number of chapters and chapters to skip
    total_chapters = 31
    skipped_chapters = total_chapters // 3

    # Calculate the total number of chapters read
    chapters_read = total_chapters - skipped_chapters

    # Calculate the total time spent reading in minutes
    minutes_spent_reading = chapters_read * 20

    # Convert minutes to hours
    hours_spent_reading = minutes_spent_reading / 60

    result = hours_spent_reading
    return result

print(solution())