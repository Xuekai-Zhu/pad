def solution():
    # Calculate the total distance that Troy walks to school and back in 5 days
    troy_distance = 2 * 75 * 5  # Troy's home is 75 meters away from school and he walks to and from school every day for 5 days

    # Calculate the total distance that Emily walks to school and back in 5 days
    emily_distance = 2 * 98 * 5  # Emily's home is 98 meters away from school and she walks to and from school every day for 5 days

    # Calculate how much farther Emily walks than Troy in 5 days
    extra_distance = emily_distance - troy_distance
    result = extra_distance
    return result

print(solution())