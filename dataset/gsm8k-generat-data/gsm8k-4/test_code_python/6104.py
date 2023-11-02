def solution():
    """Casey takes 6 hours to complete a marathon race, while Zendaya takes 1/3 times longer to cover the same distance. What is the average time the two take to complete to race?"""
    # Define Casey's time to complete the race
    casey_time = 6

    # Calculate Zendaya's time to complete the race
    zendaya_time = casey_time * (1 + 1/3)

    # Calculate the average time
    average_time = (casey_time + zendaya_time) / 2

    result = average_time
    return result

print(solution())