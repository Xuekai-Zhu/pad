def solution():
    """10 people attended class on Monday, 15 on Tuesday, and 10 on each day from Wednesday through Friday. What was the average number of people who attended class each day?"""
    total_people = 10 + 15 + (10 * 3)  # Wednesday through Friday each had 10 people
    days = 5
    average = total_people / days
    result = average
    return result

print(solution())