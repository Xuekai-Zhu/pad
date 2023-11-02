def solution():
    """10 people attended class on Monday, 15 on Tuesday, and 10 on each day from Wednesday through Friday. What was the average number of people who attended class each day?"""
    # Define the total number of people who attended class each day
    total_people = 10 + 15 + 10 + 10 + 10 + 10

    # Calculate the average number of people who attended class each day
    average_people = total_people / 6

    # Return the result
    result = average_people
    return result

print(solution())