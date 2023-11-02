def solution():
    # Calculate the temperature increase during power outage
    temp_increase = 8 * 3  # temperature increases by 8 degrees per hour during 3 hours of power outage

    # Calculate how many hours the air conditioner needs to run to bring the temperature back down
    temp_difference = 43 - temp_increase - 68  # 68 is the initial temperature before power outage
    hours_needed = temp_difference / 4  # air conditioner lowers the temperature by 4 degrees per hour

    result = hours_needed
    return result

print(solution())