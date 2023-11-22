def solution():
    
    # Define the distances traveled by each city
    city1_distance = 75
    city2_distance = 100
    city3_distance = city1_distance + city2_distance - 50

    # Calculate the total distance traveled in a day
    total_distance = city1_distance + city2_distance + city3_distance

    # Calculate the number of days the train needs to service
    service_days = total_distance // 18000

    # Display the number of days the train needs to service
    result = service_days
    return result

print(solution())