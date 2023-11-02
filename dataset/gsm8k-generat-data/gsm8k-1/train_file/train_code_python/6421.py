def solution():
    """Eric decides to go to the park. He runs for 20 minutes, then jogs for 10 minutes to reach the park. When he returns, he takes a different route home and this takes him 3 times as long as his trip there. How long does it take Eric to return home?"""
    run_time = 20
    jog_time = 10
    total_time_to_park = run_time + jog_time
    return_time_multiplier = 3
    return_time = total_time_to_park * return_time_multiplier
    result = return_time
    return result

print(solution())