def solution():
    normal_time = 5  # In normal conditions, Ann takes 5 minutes to frost a cake
    sprained_time = 8  # With a sprained wrist, Ann takes 8 minutes to frost a cake
    num_cakes = 10  # Ann needs to frost 10 cakes

    # Calculate the total time it would take Ann to frost 10 cakes with her sprained wrist
    total_sprained_time = num_cakes * sprained_time

    # Calculate the total time it would take Ann to frost 10 cakes in normal conditions
    total_normal_time = num_cakes * normal_time

    # Calculate how much longer it takes for Ann to frost 10 cakes with her sprained wrist
    extra_time = total_sprained_time - total_normal_time
    result = extra_time
    return result

print(solution())