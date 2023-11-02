def solution():
    total_acres = 8  # Jerry mows 8 acres of lawn each week
    riding_mower_acres = 0.75 * total_acres  # Jerry uses a riding mower for 3/4 of the lawn
    push_mower_acres = total_acres - riding_mower_acres  # Jerry uses a push mower for the rest of the lawn
    riding_mower_speed = 2  # Jerry's riding mower can cut 2 acres an hour
    push_mower_speed = 1  # Jerry's push mower can cut 1 acre an hour

    # Calculate the time Jerry spends mowing with the riding mower
    riding_mower_time = riding_mower_acres / riding_mower_speed

    # Calculate the time Jerry spends mowing with the push mower
    push_mower_time = push_mower_acres / push_mower_speed

    # Calculate the total time Jerry spends mowing each week
    total_time = riding_mower_time + push_mower_time
    result = total_time
    return result

print(solution())