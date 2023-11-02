def solution():
    """A book has 8 chapters. Beth has read 2 chapters in 3 hours. If she continues reading at that rate, in how many hours will she be able to finish reading the remaining chapters?"""
    # Define the number of chapters in the book
    num_chapters = 8

    # Define the number of chapters Beth has already read
    num_chapters_read = 2

    # Define the time it took Beth to read the chapters she has read
    time_taken = 3

    # Calculate the rate at which Beth is reading
    rate = (num_chapters_read / time_taken)

    # Calculate the number of hours it will take Beth to finish reading the remaining chapters
    remaining_chapters = num_chapters - num_chapters_read
    remaining_time = remaining_chapters / rate

    # Display the remaining time
    result = remaining_time
    return result

print(solution())