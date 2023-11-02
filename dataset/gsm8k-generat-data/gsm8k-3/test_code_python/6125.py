def solution():
    """Four athletes joined a relay race. Athlete 1  ran for 55 seconds, athlete 2 ran 10 seconds more than athlete 1, athlete 3 ran 15 seconds less than athlete 2, and athlete four finished it 25 seconds less than athlete 1. How long, in seconds, did it take them to finish the relay race?"""
    # Define the time each athlete took to run their leg of the relay
    time1 = 55
    time2 = time1 + 10
    time3 = time2 - 15
    time4 = time1 - 25

    # Calculate the total time taken to finish the relay
    total_time = time1 + time2 + time3 + time4

    # Display the total time taken
    result = total_time
    return result

print(solution())