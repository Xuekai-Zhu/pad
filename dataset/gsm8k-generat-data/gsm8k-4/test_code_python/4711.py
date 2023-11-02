def solution():
    """Anna is reading a 31-chapter textbook, but she skips all the chapters that are divisible by 3. If it takes her 20 minutes to read each chapter, how many hours does she spend reading total?"""
    # Define the number of chapters in the textbook
    total_chapters = 31

    # Calculate the number of chapters Anna will actually read
    chapters_read = total_chapters - (total_chapters // 3)

    # Calculate the total time spent reading
    total_time = chapters_read * 20

    # Convert the time to hours
    total_hours = total_time / 60

    # return the result
    result = total_hours
    return result

print(solution())