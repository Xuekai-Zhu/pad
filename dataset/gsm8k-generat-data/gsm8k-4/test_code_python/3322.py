def solution():
    """Tony goes on 5 rollercoasters while he is at the park. The first went 50 miles per hour. The second went 62 miles per hour. The third when 73 miles per hour. The fourth when 70 miles per hour. His average speed during the day was 59 miles per hour. How fast was the fifth coaster?"""
    # Define the total number of rollercoasters and the average speed
    total_rollercoasters = 5
    average_speed = 59

    # Calculate the total distance traveled
    total_distance = total_rollercoasters * average_speed

    # Calculate the distance traveled on the first 4 rollercoasters
    first_four_distance = 50 + 62 + 73 + 70

    # Calculate the speed of the fifth rollercoaster
    fifth_speed = (total_distance - first_four_distance) / (total_rollercoasters - 4)

    result = fifth_speed
    return result

print(solution())