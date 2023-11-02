def solution():
    first_half_flow = 2  # cups per 10 minutes
    second_half_flow = 4  # cups per 10 minutes
    total_time = 120  # minutes

    # Calculate the total amount of water that flowed in the first half
    first_half_water = (first_half_flow * 3) + (second_half_flow * 6)

    # Calculate the total amount of water that flowed in the second half
    second_half_water = second_half_flow * 6

    # Calculate the total amount of water that flowed in both halves
    total_water_flow = first_half_water + second_half_water

    # Calculate the amount of water that Shawn has to dump
    water_to_dump = total_water_flow / 2

    # Calculate the amount of water that is left
    water_left = total_water_flow - water_to_dump
    result = water_left
    return result

print(solution())