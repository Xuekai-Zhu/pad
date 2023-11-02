def solution():
    """Carlo has a music recital next week. He practiced twice as long on Monday as on Tuesday. On Tuesday, he practiced 10 minutes less than on Wednesday. On Wednesday, he practiced 5 minutes more than on Thursday. On Thursday, he practiced for 50 minutes. If he needs to practice for a total of 5 hours that week, how long should Carlo practice on Friday?"""
    # Define the number of minutes practiced on Thursday
    thursday_minutes = 50

    # Calculate the number of minutes practiced on Wednesday
    wednesday_minutes = thursday_minutes + 5

    # Calculate the number of minutes practiced on Tuesday
    tuesday_minutes = wednesday_minutes - 10

    # Calculate the number of minutes practiced on Monday
    monday_minutes = tuesday_minutes * 2

    # Calculate the total number of minutes practiced so far
    total_minutes = thursday_minutes + wednesday_minutes + tuesday_minutes + monday_minutes

    # Calculate the number of minutes Carlo needs to practice on Friday
    friday_minutes = (5 * 60) - total_minutes

    result = friday_minutes
    return result

print(solution())