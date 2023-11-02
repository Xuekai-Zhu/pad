def solution():
    """Janet goes to the gym for 5 hours a week. She goes Monday, Tuesday, Wednesday, and Friday. She spends an hour and a half each day on Monday and Wednesday.
    If she spends the same amount of time at the gym on Tuesday and Friday how many hours is she at the gym on Friday?"""
    # Define the time spent at gym on Monday and Wednesday
    monday_time = 1.5
    wednesday_time = 1.5

    # Calculate the total time spent at gym on Monday, Tuesday, Wednesday, and Friday
    total_time = 5

    # Calculate the time spent at gym on Tuesday
    tuesday_time = (total_time - monday_time - wednesday_time) / 2

    # Calculate the time spent at gym on Friday
    friday_time = tuesday_time

    # return the result
    result = friday_time
    return result

print(solution())