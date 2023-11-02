def solution():
    # Calculate the number of chapters Anna reads
    num_chapters = 20 
    for i in range(1, 32):
        if i % 3 != 0:
            num_chapters += 1

    # Calculate the total amount of time Anna spends reading
    total_time = num_chapters * 20  # it takes her 20 minutes to read each chapter
    hours = total_time / 60  # convert minutes to hours
    result = hours
    return result

print(solution())