def solution():
    time_ny_sf = 24  # time to travel from NY to SF
    time_nola_ny = (3/4) * time_ny_sf  # time to travel from NOLA to NY

    total_time = time_ny_sf + 16 + time_nola_ny  # total time including layover
    result = total_time

    return result

print(solution())