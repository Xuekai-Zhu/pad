def solution():
    """Tony goes on 5 rollercoasters while he is at the park. The first went 50 miles per hour. The second went 62 miles per hour. The third when 73 miles per hour. The fourth when 70 miles per hour. His average speed during the day was 59 miles per hour. How fast was the fifth coaster?"""
    # Calculate the total distance traveled on the first 4 coasters
    total_distance = 4*59

    # Calculate the total time spent on the first 4 coasters
    total_time = (50/60) + (62/60) + (73/60) + (70/60)

    # Calculate the average speed required to reach an average speed of 59 mph
    required_speed = (total_distance / (5-total_time)) * 60

    # Calculate the speed of the fifth coaster
    fifth_coaster_speed = required_speed - ((50+62+73+70)/4)

    # Display the speed of the fifth coaster
    result = fifth_coaster_speed
    return result

print(solution())