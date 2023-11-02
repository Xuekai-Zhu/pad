def solution():
    """Michael is stuck in an elevator that is slowly moving to the bottom floor. The elevator needs to move down 20 floors to reach the bottom. It takes 15 minutes for the elevator to travel down the first half of the floors. The elevator then takes 5 minutes per floor to travel down the next 5 floors. It then takes 16 minutes per floor for the elevator to finish traveling down the final 5 floors. In hours, how long did it take for the elevator to reach the bottom?"""
    # Define the number of floors and time per floor for each section of the elevator ride
    total_floors = 20
    first_half_floors = total_floors / 2
    second_half_floors = total_floors - first_half_floors
    first_half_time = 15
    second_half_time1 = 5
    second_half_time2 = 16

    # Calculate the total time for the first half of the elevator ride
    first_half_total_time = first_half_floors * first_half_time

    # Calculate the total time for the second half of the elevator ride
    second_half_total_time = (second_half_floors - 5) * second_half_time1 + (5 * second_half_time2)

    # Calculate the total time for the entire elevator ride in minutes
    total_time_minutes = first_half_total_time + second_half_total_time

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    # return the result
    result = total_time_hours
    return result

print(solution())