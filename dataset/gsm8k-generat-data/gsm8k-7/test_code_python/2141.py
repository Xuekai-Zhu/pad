def solution():
    total_acres = 8
    riding_mower_portion = 0.75
    riding_mower_speed = 2
    push_mower_speed = 1

    # Calculate the number of acres mowed with riding mower
    acres_with_riding_mower = total_acres * riding_mower_portion

    # Calculate the time spent mowing with riding mower
    time_with_riding_mower = acres_with_riding_mower / riding_mower_speed

    # Calculate the number of acres mowed with push mower
    acres_with_push_mower = total_acres - acres_with_riding_mower

    # Calculate the time spent mowing with push mower
    time_with_push_mower = acres_with_push_mower / push_mower_speed

    # Calculate the total time spent mowing
    total_time = time_with_riding_mower + time_with_push_mower
    result = total_time
    return result

print(solution())