def solution():
    first_intersection = 40

    # Calculate the number of road signs at the second intersection
    second_intersection = first_intersection * (1 + 1/4)

    # Calculate the number of road signs at the third intersection
    third_intersection = 2 * second_intersection

    # Calculate the number of road signs at the fourth intersection
    fourth_intersection = third_intersection - 20

    # Calculate the total number of road signs at all four intersections
    total_road_signs = first_intersection + second_intersection + third_intersection + fourth_intersection
    result = total_road_signs
    return result

print(solution())