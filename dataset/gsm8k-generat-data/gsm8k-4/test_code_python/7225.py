def solution():
    """The Zargon Destroyer spacecraft can travel at 2 billion miles per hour in normal space, but when moving through a black hole they travel three times faster. If the Zargon Destroyer is making a voyage that travels seven hours in normal space and two hours through a black hole, how many billions of miles would they have traveled?"""
    # Define the speed of the Zargon Destroyer in normal space and in a black hole
    normal_space_speed = 2
    black_hole_speed = normal_space_speed * 3

    # Define the duration of the voyage in normal space and in a black hole
    normal_space_duration = 7
    black_hole_duration = 2

    # Calculate the distance traveled in normal space and in a black hole
    normal_space_distance = normal_space_duration * normal_space_speed
    black_hole_distance = black_hole_duration * black_hole_speed

    # Calculate the total distance traveled
    total_distance = normal_space_distance + black_hole_distance

    # Convert the total distance to billions of miles
    total_distance_billions = total_distance / 1000000000

    # return the result
    result = total_distance_billions
    return result

print(solution())