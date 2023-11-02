def solution():
    initial_tank_volume = 4000
    large_tanker_capacity = 20000
    large_tanker_initial_volume = 3000
    oil_poured = 0.75 * initial_tank_volume

    # Calculate the current volume of oil in the large tanker
    current_volume = large_tanker_initial_volume + oil_poured

    # Calculate how much more oil is needed to make the large tanker half-full
    half_tanker_volume = large_tanker_capacity / 2.0
    more_oil_needed = half_tanker_volume - current_volume
    result = more_oil_needed
    return result

print(solution())