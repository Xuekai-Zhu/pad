def solution():
    
    # Define the distances traveled in the first 4 days
    distance_first_4_days = 200

    # Calculate the total distance traveled in the next 2 days
    distance_next_2_days = distance_first_4_days * 0.3

    # Calculate the total distance traveled in the first 2 days
    total_distance_first_2_days = distance_first_4_days + distance_next_2_days

    # Calculate the total distance made during the second week
    distance_second_week = 300

    # Calculate the total distance traveled during the two-week-long trip
    total_distance = total_distance_first_4_days + total_distance_next_2_days + distance_second_week

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())