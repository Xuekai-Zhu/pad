def solution():
    """Casey takes 6 hours to complete a marathon race, while Zendaya takes 1/3 times longer to cover the same distance. What is the average time the two take to complete to race?"""
    # Define Casey's time and calculate Zendaya's time
    casey_time = 6
    zendaya_time = casey_time * (4/3)

    # Calculate the average time
    avg_time = (casey_time + zendaya_time) / 2

    # Display the average time
    result = avg_time
    return result

print(solution())