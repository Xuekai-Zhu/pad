def solution():
    # Define the normal frosting time and the injured frosting time
    normal_time = 5
    injured_time = 8

    # Calculate the time it takes Ann to frost 10 cakes with her sprained wrist
    time_for_10_cakes = 10 * injured_time

    # Calculate the additional time it takes Ann to frost 10 cakes with her sprained wrist
    additional_time = time_for_10_cakes - (10 * normal_time)

    result = additional_time
    return result

print(solution())