def solution():
    """Eric decides to go to the park. He runs for 20 minutes, then jogs for 10 minutes to reach the park. When he returns, he takes a different route home and this takes him 3 times as long as his trip there. How long does it take Eric to return home?"""
    # Define the time it takes Eric to run and jog to the park
    time_to_park = 20 + 10  # 30 minutes

    # Define the time it takes Eric to return home (in relation to his time to the park)
    return_time_factor = 3

    # Calculate the time it takes Eric to return home
    return_time = time_to_park * return_time_factor

    # return the result
    result = return_time
    return result

print(solution())