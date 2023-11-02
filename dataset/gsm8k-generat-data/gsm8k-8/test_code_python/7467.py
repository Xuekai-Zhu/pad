def solution():
    # Calculate the temperature increase during the power outage
    temp_increase = 8 * 3

    # Calculate the temperature above the target temperature of 43°F
    temp_above_target = temp_increase - (43 - 35)

    # Calculate the time it will take to lower the temperature back to 43°F
    time_to_restore = temp_above_target / 4

    result = time_to_restore
    return result

print(solution())