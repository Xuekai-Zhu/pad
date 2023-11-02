def solution():
    num_chapters = 31
    time_per_chapter = 20  # in minutes

    # Calculate the number of chapters Anna will actually read
    num_filtered_chapters = num_chapters - (num_chapters // 3)

    # Calculate the total time in minutes that Anna will spend reading
    total_time = num_filtered_chapters * time_per_chapter

    # Convert the total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())