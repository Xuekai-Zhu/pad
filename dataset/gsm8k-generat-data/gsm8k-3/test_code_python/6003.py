def solution():
    """Mr. Isaac rides his bicycle at the rate of 10 miles per hour for 30 minutes. If he rides for another 15 miles, rests for 30 minutes, and then covers the remaining distance of 20 miles, what's the total time in minutes took to travel the whole journey?"""
    # Calculate the time taken to ride the first 5 miles
    time1 = (5 / 10) * 60  # distance / speed * 60 to convert hours to minutes

    # Calculate the time taken to ride the next 15 miles
    time2 = (15 / 10) * 60

    # Calculate the time taken for the rest period
    time3 = 30

    # Calculate the time taken to ride the final 20 miles
    time4 = (20 / 10) * 60

    # Calculate the total time taken
    total_time = time1 + time2 + time3 + time4

    # Display the total time taken
    result = total_time
    return result

print(solution())