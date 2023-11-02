def solution():
    """Eric decides to go to the park. He runs for 20 minutes, then jogs for 10 minutes to reach the park. When he returns, he takes a different route home and this takes him 3 times as long as his trip there. How long does it take Eric to return home?"""
    # Calculate the time it takes for Eric to get to the park
    time_to_park = 20 + 10  # 20 minutes running + 10 minutes jogging

    # Calculate the time it takes for Eric to return home
    time_return = time_to_park * 3  # 3 times longer than the trip to the park

    # Display the time it takes for Eric to return home
    result = time_return
    return result

print(solution())