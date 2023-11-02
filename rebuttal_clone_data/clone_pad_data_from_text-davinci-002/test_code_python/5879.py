def solution():
    total_spots = 30
    upper_torso_spots = total_spots / 2
    back_and_hindquarters_spots = upper_torso_spots / 3
    side_spots = total_spots - upper_torso_spots - back_and_hindquarters_spots
    result = side_spots
    return result

print(solution())