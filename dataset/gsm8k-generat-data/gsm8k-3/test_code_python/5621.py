def solution():
    """Lawrence worked 8 hours each day on Monday, Tuesday and Friday. He worked 5.5 hours on both Wednesday and Thursday. How many hours would Lawrence work each day if he worked the same number of hours each day?"""
    # Calculate the total number of hours Lawrence worked
    total_hours = 8*3 + 5.5*2

    # Divide the total hours by the number of days worked to find the average number of hours per day
    avg_hours = total_hours / 5

    # Display the average number of hours worked per day
    result = avg_hours
    return result

print(solution())