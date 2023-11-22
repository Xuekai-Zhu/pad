def solution():
    
    # Define the average speed of the first car and the second car
    car1_speed = 60
    car2_speed = 70

    # Define the time it takes for each car to complete the trip
    time = 2

    # Calculate the distance each car will travel in 2 hours
    car1_distance = car1_speed * time
    car2_distance = car2_speed * time

    # Calculate the total distance they will be split on the highway after 2 hours
    total_distance = car1_distance + car2_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())