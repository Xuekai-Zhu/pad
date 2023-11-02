def solution():
    # Calculate the total time Laura spent on her trips to the park
    total_time = (2 + 0.5) * 6  # 2 hours at the park + 0.5 hours walking to and from the park, multiplied by 6 trips

    # Calculate the total time Laura spent in the park
    park_time = 2 * 6  # 2 hours at the park, multiplied by 6 trips

    # Calculate the percentage of time Laura spent in the park
    percentage_in_park = (park_time / total_time) * 100

    result = percentage_in_park
    return result

print(solution())