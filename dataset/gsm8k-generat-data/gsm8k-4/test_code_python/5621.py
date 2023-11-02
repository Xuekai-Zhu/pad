def solution():
    """Lawrence worked 8 hours each day on Monday, Tuesday and Friday. He worked 5.5 hours on both Wednesday and Thursday. How many hours would Lawrence work each day if he worked the same number of hours each day?"""
    # Calculate the total number of hours worked in a week
    total_hours = 8*3 + 5.5*2

    # Calculate the average number of hours worked per day
    average_hours = total_hours / 5

    # Return the result
    result = average_hours
    return result

print(solution())