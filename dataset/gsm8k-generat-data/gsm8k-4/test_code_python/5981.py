def solution():
    """Cortney is downloading some files to her computer. Her internet speed is 2 megabits per minute. If she can download the files one at a time and the files she is downloading have the size of 80 megabits, 90 megabits, and 70 megabits. How many hours will it take for her to download all of it?"""
    # Define the internet speed in megabits per minute
    speed = 2

    # Define the size of each file in megabits
    file1_size = 80
    file2_size = 90
    file3_size = 70

    # Calculate the total download time for each file in minutes
    file1_time = file1_size / speed
    file2_time = file2_size / speed
    file3_time = file3_size / speed

    # Calculate the total download time in minutes
    total_time = file1_time + file2_time + file3_time

    # Convert the total download time to hours
    hours = total_time / 60

    # return the result
    result = hours
    return result

print(solution())