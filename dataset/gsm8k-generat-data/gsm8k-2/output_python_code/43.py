def solution():
    """An earthquake caused four buildings to collapse. Experts predicted that each following earthquake would have double the number of collapsing buildings as the previous one, since each one would make the foundations less stable. After three more earthquakes, how many buildings had collapsed including those from the first earthquake?"""
    first_earthquake = 4
    second_earthquake = first_earthquake * 2
    third_earthquake = second_earthquake * 2
    fourth_earthquake = third_earthquake * 2
    total_buildings = first_earthquake + second_earthquake + third_earthquake + fourth_earthquake
    result = total_buildings
    return result

print(solution())