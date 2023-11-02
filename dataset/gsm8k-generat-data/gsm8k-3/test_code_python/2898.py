def solution():
    """Michael is stuck in an elevator that is slowly moving to the bottom floor. The elevator needs to move down 20 floors to reach the bottom. It takes 15 minutes for the elevator to travel down the first half of the floors. The elevator then takes 5 minutes per floor to travel down the next 5 floors. It then takes 16 minutes per floor for the elevator to finish traveling down the final 5 floors. In hours, how long did it take for the elevator to reach the bottom?"""
    # Calculate the time it takes to travel down the first half of the floors
    time_half = 15 / 60

    # Calculate the time it takes to travel down the next 5 floors
    time_5_floors = 5 * 5 / 60

    # Calculate the time it takes to travel down the final 5 floors
    time_last_5_floors = 16 * 5 / 60

    # Calculate the total time it takes to reach the bottom
    total_time = time_half + time_5_floors + time_last_5_floors

    # Display the total time in hours
    result = total_time
    return result

print(solution())