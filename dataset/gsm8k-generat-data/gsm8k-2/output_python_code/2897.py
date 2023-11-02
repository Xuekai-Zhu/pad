def solution():
    """Michael is stuck in an elevator that is slowly moving to the bottom floor. The elevator needs to move down 20 floors to reach the bottom. It takes 15 minutes for the elevator to travel down the first half of the floors. The elevator then takes 5 minutes per floor to travel down the next 5 floors. It then takes 16 minutes per floor for the elevator to finish traveling down the final 5 floors. In hours, how long did it take for the elevator to reach the bottom?"""
    total_floors = 20
    first_half_floors = total_floors // 2
    second_half_floors = total_floors - first_half_floors
    first_half_time = 15
    second_half_time = (second_half_floors-5)*5 + 5*16
    total_time = (first_half_floors*first_half_time) + (second_half_floors*second_half_time)
    result = total_time / 60 # converting minutes to hours
    return result

print(solution())