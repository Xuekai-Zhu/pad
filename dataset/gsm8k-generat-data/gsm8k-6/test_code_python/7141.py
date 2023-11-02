def solution():
    # Calculate the time it takes Ann to frost one cake with her sprained wrist
    time_per_cake = 8  # it takes 8 minutes to frost one cake with a sprained wrist

    # Calculate the total time it will take Ann to frost 10 cakes
    total_time = time_per_cake * 10

    # Calculate how much longer it will take Ann to frost 10 cakes with her sprained wrist compared to her normal time
    normal_time_per_cake = 5  # normally Ann can frost a cake in 5 minutes
    extra_time_per_cake = time_per_cake - normal_time_per_cake
    extra_time_for_10_cakes = extra_time_per_cake * 10
    result = extra_time_for_10_cakes
    return result

print(solution())