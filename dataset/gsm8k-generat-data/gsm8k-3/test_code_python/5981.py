def solution():
    """Cortney is downloading some files to her computer. Her internet speed is 2 megabits per minute. If she can download the files one at a time and the files she is downloading have the size of 80 megabits, 90 megabits, and 70 megabits. How many hours will it take for her to download all of it?"""
    # Define the internet speed and the file sizes
    INTERNET_SPEED = 2 # megabits per minute
    FILE_SIZES = [80, 90, 70] # megabits

    # Calculate the total size of all the files
    total_size = sum(FILE_SIZES)

    # Calculate the total download time in minutes
    download_time_minutes = total_size / INTERNET_SPEED

    # Convert minutes to hours
    download_time_hours = download_time_minutes / 60

    # Display the total download time in hours
    result = download_time_hours
    return result

print(solution())