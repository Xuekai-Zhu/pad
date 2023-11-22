def solution():
    
    # Define the number of dogs and the daily distances
    num_dogs = 4
    daily_distance = 3

    # Calculate the total distance each dog needs per day
    total_distance = 1 + 4 + 3

    # Calculate the average distance each dog needs per day
    avg_distance = daily_distance * num_dogs

    # Calculate the distance the last dog needs per day
    last_dog_distance = avg_distance

    # Display the distance the last dog needs per day
    result = last_dog_distance
    return result

print(solution())