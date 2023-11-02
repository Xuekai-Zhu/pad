def solution():
    normal_time_per_cake = 5
    sprained_time_per_cake = 8
    num_cakes = 10

    # Calculate the total time it would take Ann to frost 10 cakes with her normal wrist
    normal_time = num_cakes * normal_time_per_cake

    # Calculate the total time it would take Ann to frost 10 cakes with her sprained wrist
    sprained_time = num_cakes * sprained_time_per_cake

    # Calculate the extra time it would take her with her sprained wrist
    extra_time = sprained_time - normal_time
    result = extra_time
    return result

print(solution())