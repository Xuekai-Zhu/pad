def solution():
    # Calculate the number of road signs at the second intersection
    road_signs_2 = 40 + (1/4)*40

    # Calculate the number of road signs at the third intersection
    road_signs_3 = 2*road_signs_2

    # Calculate the number of road signs at the fourth intersection
    road_signs_4 = road_signs_3 - 20

    # Calculate the total number of road signs at the four intersections
    total_road_signs = 40 + road_signs_2 + road_signs_3 + road_signs_4
    result = total_road_signs
    return result

print(solution())