def solution():
    
    # Define the number of times Chase and Rider ride their bikes each day
    chase_rides = 5
    rider_rides = 2 * chase_rides

    # Calculate the total number of times they ride their bikes in a week
    total_rides = (chase_rides + rider_rides) * 7

    # Display the total number of times they ride their bikes in a week
    result = total_rides
    return result

print(solution())