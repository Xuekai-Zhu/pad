def solution():
    # Define the weight Tony can lift in "the curl"
    curl_weight = 90

    # Define the weight Tony can lift in "the military press"
    military_press_weight = curl_weight * 2

    # Define the weight Tony can lift in "the squat"
    squat_weight = military_press_weight * 5

    result = squat_weight
    return result

print(solution())