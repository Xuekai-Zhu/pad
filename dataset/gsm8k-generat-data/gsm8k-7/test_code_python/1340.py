def solution():
    max_riding_time = 6
    used_max_time = 2
    half_max_time = 2
    reduced_time = 0
    two_hours = 1.5

    # Calculate the total riding time used for the two days with only 1.5 hours of riding
    reduced_time += two_hours * 2

    # Calculate the total riding time used for the two days with half maximum riding time
    reduced_time += half_max_time * (max_riding_time / 2)

    # Calculate the total riding time used for the two days with maximum riding time
    used_max_time *= max_riding_time

    # Calculate the total riding time
    total_riding_time = used_max_time + reduced_time

    # Calculate the total riding time over the 6 days
    six_day_riding_time = total_riding_time * 3

    result = six_day_riding_time
    return result

print(solution())