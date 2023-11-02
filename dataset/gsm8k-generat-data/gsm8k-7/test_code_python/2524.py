def solution():
    num_balloons = 50
    helium_volume = 1800
    helium_per_balloon = 50
    remaining_volume_per_balloon = 100  # Assuming each balloon takes 50cm³ of helium and 50cm³ of ordinary air

    # Calculate the maximum number of balloons that can be filled with helium
    max_helium_balloons = helium_volume / helium_per_balloon

    if max_helium_balloons > num_balloons:
        num_helium_balloons = num_balloons
        num_remaining_balloons = 0
    else:
        num_helium_balloons = max_helium_balloons
        num_remaining_balloons = num_balloons - max_helium_balloons

    # Calculate the number of balloons touching the ceiling
    num_touching_ceiling = num_helium_balloons

    result = num_touching_ceiling - num_remaining_balloons
    return result

print(solution())