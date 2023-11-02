def solution():
    """Oliver is working out in a gym. On Monday he worked out for 4 hours, and the next day for 2 hours less. On Wednesday he decided to work out twice as much as on Monday. On Thursday the gym was closed, so Oliver needed to exercise at home which took twice as much time as on Tuesday. How many hours in total have Oliver worked out during these four days?"""
    # Define the number of hours Oliver worked out each day
    monday_hours = 4
    tuesday_hours = monday_hours - 2
    wednesday_hours = 2 * monday_hours
    thursday_hours = 2 * tuesday_hours

    # Calculate the total number of hours Oliver worked out
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours

    # Display the total number of hours
    result = total_hours
    return result

print(solution())