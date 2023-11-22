def solution():
    
    # Define the distance traveled by each train per hour
    distance_train1 = 60
    distance_train2 = distance_train1 / 2

    # Calculate the total distance traveled by both trains after 3 hours
    total_distance = (distance_train1 + distance_train2) * 3

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())