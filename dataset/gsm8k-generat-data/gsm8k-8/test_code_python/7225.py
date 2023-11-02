def solution():
    # Define the speed of the Zargon Destroyer in normal space and through a black hole
    normal_speed = 2
    black_hole_speed = normal_speed * 3

    # Define the duration of the voyage in normal space and through a black hole
    normal_duration = 7
    black_hole_duration = 2

    # Calculate the distance traveled in normal space and through a black hole
    normal_distance = normal_speed * normal_duration
    black_hole_distance = black_hole_speed * black_hole_duration

    # Calculate the total distance traveled
    total_distance = normal_distance + black_hole_distance

    # Convert the total distance from miles to billions of miles
    total_distance_billions = total_distance / 1000000000

    result = total_distance_billions
    return result

print(solution())