def solution():
    """Harry is counting the hours that he sleeps. On Monday night, he sleeps for 8 hours. On Tuesday night, he sleeps for 7 hours. On Wednesday night, he sleeps for 8 hours. On Thursday night, he sleeps for 10 hours. On Friday night he sleeps for 7 hours. What is the average number of hours that Harry sleeps in one night?"""
    # Calculate the total number of hours slept
    total_hours = 8 + 7 + 8 + 10 + 7

    # Calculate the average number of hours slept
    average_hours = total_hours / 5

    # Display the average number of hours slept
    result = average_hours
    return result

print(solution())