def solution():
    initial_volume = 4000  # Initial volume of the tank
    transferred_volume = 0.75 * initial_volume  # Volume of oil transferred to the large tanker
    large_tanker_initial_volume = 20000  # Initial volume of the large tanker
    large_tanker_current_volume = transferred_volume + 3000  # Volume of oil in the large tanker after transfer
    volume_required_for_half_tanker = large_tanker_initial_volume / 2 - large_tanker_current_volume

    # Calculate the additional volume of oil required to make the large tanker half-full
    result = volume_required_for_half_tanker
    return result

print(solution())