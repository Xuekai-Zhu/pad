def solution():
    
    # Define the distances traveled from each city
    city1_distance = 75
    city2_distance = 100
    city3_distance = (city1_distance + city2_distance) - 50

    # Calculate the total distance traveled per day
    total_distance = city1_distance + city2_distance + city3_distance + city4_distance

    # Calculate the number of days it will go between services
    days_between_services = total_distance / 18000

    # Display the number of days it will go between services
    result = days_between_services
    return result

print(solution())