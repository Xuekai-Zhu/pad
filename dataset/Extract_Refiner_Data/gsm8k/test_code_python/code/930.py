def solution():
    
    # Define the number of watermelons each person gets
    zoey_watermelons = 40
    sydney_watermelons = 35

    # Define the distances spit each person
    zoey_distance = 10
    sydney_distance = 12

    # Calculate the total distance spat
    total_distance = (zoey_watermelons * zoey_distance) + (sydney_watermelons * sydney_distance)

    # Calculate the average total distance spat
    average_distance = total_distance / 2

    # Display the average total distance spat
    result = average_distance
    return result

print(solution())