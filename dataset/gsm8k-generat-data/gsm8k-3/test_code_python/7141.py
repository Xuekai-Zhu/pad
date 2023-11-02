def solution():
    """Normally Ann can frost a cake in 5 minutes. However, today she has a sprained wrist and it takes her 8 minutes to frost a cake. How much longer would it take her to frost 10 cakes with her sprained wrist?"""
    # Define the time it takes Ann to frost one cake normally
    normal_time = 5

    # Define the time it takes Ann to frost one cake with a sprained wrist
    sprained_time = 8

    # Calculate the extra time it takes Ann to frost one cake with a sprained wrist
    extra_time = sprained_time - normal_time

    # Calculate how long it would take Ann to frost 10 cakes with a sprained wrist
    total_time = 10 * sprained_time

    # Calculate how much longer it would take Ann to frost 10 cakes with a sprained wrist compared to her normal time
    extra_total_time = total_time - 10 * normal_time

    # Display how much longer it would take Ann to frost 10 cakes with a sprained wrist compared to her normal time
    result = extra_total_time
    return result

print(solution())