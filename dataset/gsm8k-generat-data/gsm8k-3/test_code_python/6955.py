def solution():
    """Carlo has a music recital next week. He practiced twice as long on Monday as on Tuesday. On Tuesday, he practiced 10 minutes less than on Wednesday. On Wednesday, he practiced 5 minutes more than on Thursday. On Thursday, he practiced for 50 minutes. If he needs to practice for a total of 5 hours that week, how long should Carlo practice on Friday?"""
    # Define the total practice time in minutes for the week
    TOTAL_TIME = 5 * 60

    # Calculate the practice time on Thursday
    thursday_time = 50

    # Calculate the practice time on Wednesday
    wednesday_time = thursday_time + 5

    # Calculate the practice time on Tuesday
    tuesday_time = wednesday_time - 10

    # Calculate the practice time on Monday
    monday_time = 2 * tuesday_time

    # Calculate the total practice time for the first four days
    total_time_first_four_days = monday_time + tuesday_time + wednesday_time + thursday_time

    # Calculate the practice time needed on Friday
    friday_time = (TOTAL_TIME - total_time_first_four_days) / 60

    # Display the practice time on Friday
    result = friday_time
    return result

print(solution())