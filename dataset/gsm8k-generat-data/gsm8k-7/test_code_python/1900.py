def solution():
    temp_50_yards = 20
    temp_80_yards = temp_50_yards * 2

    sat_num_throws = 20
    sat_total_yards = sat_num_throws * temp_50_yards

    sun_num_throws = 30
    sun_total_yards = sun_num_throws * temp_80_yards

    total_yards = sat_total_yards + sun_total_yards
    result = total_yards
    return result

print(solution())