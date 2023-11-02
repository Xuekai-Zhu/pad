def solution():
    """On the weekend, Tony will walk to the store. On weekdays, he runs to the store. When he walks, he goes 2 MPH. When he runs he goes 10 MPH. The store is 4 miles away. If he goes on Sunday, Tuesday, and Thursday, what is the average time in minutes that he spends to get to the store?"""
    # Define the distance to the store
    distance = 4

    # Define the speed for walking and running
    walking_speed = 2
    running_speed = 10

    # Calculate the time it takes to walk and run to the store
    time_walking = distance / walking_speed
    time_running = distance / running_speed

    # Calculate the total time spent going to the store on all three days
    total_time = time_walking + time_running + time_running + time_running

    # Calculate the average time spent going to the store
    average_time = total_time / 3 * 60

    # Return the result
    result = round(average_time, 2)
    return result

print(solution())