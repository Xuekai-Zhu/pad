def solution():
    first_shot = 180
    second_shot = first_shot / 2
    second_shot_land = 20
    total_distance = first_shot + (second_shot + second_shot_land)

    result = total_distance
    return result

print(solution())