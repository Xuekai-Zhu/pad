def solution():
    """Michael is stuck in an elevator that is slowly moving to the bottom floor. The elevator needs to move down 20 floors to reach the bottom. It takes 15 minutes for the elevator to travel down the first half of the floors. The elevator then takes 5 minutes per floor to travel down the next 5 floors. It then takes 16 minutes per floor for the elevator to finish traveling down the final 5 floors. In hours, how long did it take for the elevator to reach the bottom?"""
    floors_to_travel = 20
    first_half_floors = floors_to_travel // 2
    second_half_floors = floors_to_travel - first_half_floors
    time_first_half = 15
    time_second_half = (second_half_floors * 5) + (5 * 60)
    time_last_floors = (first_half_floors - second_half_floors) * 16
    total_time = (time_first_half + time_second_half + time_last_floors) / 60 / 60
    result = total_time
    return result

print(solution())