def solution():
    """During my workout yesterday, I did 30 squats. Each day, I plan to increase my number of squats by 5 more than the previous day. If I do my workout for four consecutive days, how many squats will I perform the day after tomorrow?"""
    # Define the number of squats done on the first day
    squats = 30

    # Calculate the number of squats done on the second day
    squats += 5

    # Calculate the number of squats done on the third day
    squats += 10

    # Calculate the number of squats I will perform the day after tomorrow
    squats += 15

    # Display the number of squats I will perform the day after tomorrow
    result = squats
    return result

print(solution())