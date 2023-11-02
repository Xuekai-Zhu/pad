def solution():
    """Madison and Gigi have to run a total of 2400 meters in gym class. The track is 150 meters around. If they each have run 6 laps, how many more laps do they have to run before they reach 2400 meters?"""
    # Define the total distance to be covered
    total_distance = 2400

    # Define the distance covered in one lap
    lap_distance = 150

    # Define the number of laps already completed by each student
    Madison_laps = 6
    Gigi_laps = 6

    # Calculate the total distance covered by each student so far
    Madison_distance = Madison_laps * lap_distance
    Gigi_distance = Gigi_laps * lap_distance

    # Calculate the distance remaining for each student to complete the total distance
    Madison_remaining = total_distance - Madison_distance
    Gigi_remaining = total_distance - Gigi_distance

    # Calculate the number of laps remaining for each student
    Madison_laps_remaining = Madison_remaining // lap_distance
    Gigi_laps_remaining = Gigi_remaining // lap_distance

    # Calculate the total number of laps remaining for both students
    total_laps_remaining = Madison_laps_remaining + Gigi_laps_remaining

    result = total_laps_remaining
    return result

print(solution())