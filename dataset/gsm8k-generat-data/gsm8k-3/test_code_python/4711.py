def solution():
    """Anna is reading a 31-chapter textbook, but she skips all the chapters that are divisible by 3. If it takes her 20 minutes to read each chapter, how many hours does she spend reading total?"""
    # Define the number of chapters in the textbook
    NUM_CHAPTERS = 31

    # Define the time (in minutes) it takes Anna to read each chapter
    TIME_PER_CHAPTER = 20

    # Calculate the number of chapters Anna reads
    num_read_chapters = NUM_CHAPTERS - (NUM_CHAPTERS // 3)

    # Calculate the total time (in minutes) Anna spends reading
    total_time = num_read_chapters * TIME_PER_CHAPTER

    # Convert the total time to hours
    hours = total_time / 60

    # Display the total hours spent reading
    result = hours
    return result

print(solution())