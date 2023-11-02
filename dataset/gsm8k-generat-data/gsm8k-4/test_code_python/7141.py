def solution():
    """Normally Ann can frost a cake in 5 minutes. However, today she has a sprained wrist and it takes her 8 minutes to frost a cake. How much longer would it take her to frost 10 cakes with her sprained wrist?"""
    # Define the time it takes Ann to frost a cake and the number of cakes she needs to frost
    normal_time = 5
    sprained_time = 8
    num_cakes = 10

    # Calculate the total time it would take Ann to frost 10 cakes with a sprained wrist
    total_sprained_time = sprained_time * num_cakes

    # Calculate the total time it would take Ann to frost 10 cakes with a normal wrist
    total_normal_time = normal_time * num_cakes

    # Calculate the additional time it would take Ann to frost 10 cakes with a sprained wrist
    additional_time = total_sprained_time - total_normal_time

    # return the result
    result = additional_time
    return result

print(solution())