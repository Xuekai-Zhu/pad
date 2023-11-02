def solution():
    """Eric decides to go to the park. He runs for 20 minutes, then jogs for 10 minutes to reach the park. When he returns, he takes a different route home and this takes him 3 times as long as his trip there. How long does it take Eric to return home?"""
    run_time = 20
    jog_time = 10
    to_park_time = run_time + jog_time
    return_time = to_park_time * 3
    result = return_time
    return result

print(solution())