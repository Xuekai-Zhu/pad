def solution():
    """On the weekend, Tony will walk to the store. On weekdays, he runs to the store. When he walks, he goes 2 MPH. When he runs he goes 10 MPH. The store is 4 miles away. If he goes on Sunday, Tuesday, and Thursday, what is the average time in minutes that he spends to get to the store?"""
    # Define the distances to the store on each day
    sunday_distance = 4
    tuesday_distance = 4
    thursday_distance = 4

    # Calculate the times it takes to get to the store on each day
    sunday_time = sunday_distance / 2 * 60 # Convert hours to minutes
    tuesday_time = tuesday_distance / 10 * 60 # Convert hours to minutes
    thursday_time = thursday_distance / 10 * 60 # Convert hours to minutes

    # Calculate the average time to get to the store
    total_time = sunday_time + tuesday_time + thursday_time
    average_time = total_time / 3

    # Display the average time
    result = average_time
    return result

print(solution())