def solution():
    curl_weight = 90  # Tony can curl 90 pounds
    military_press_weight = 2 * curl_weight  # Tony can lift twice the weight he can curl in the military press
    squat_weight = 5 * military_press_weight  # Tony can squat 5 times the weight he can lift in the military press
    result = squat_weight
    return result

print(solution())