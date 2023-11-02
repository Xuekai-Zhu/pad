def solution():
    """Four athletes joined a relay race. Athlete 1 ran for 55 seconds, athlete 2 ran 10 seconds more than athlete 1, athlete 3 ran 15 seconds less than athlete 2, and athlete four finished it 25 seconds less than athlete 1. How long, in seconds, did it take them to finish the relay race?"""
    # Define the time for athlete 1
    athlete1_time = 55

    # Define the time for athlete 2
    athlete2_time = athlete1_time + 10

    # Define the time for athlete 3
    athlete3_time = athlete2_time - 15

    # Define the time for athlete 4
    athlete4_time = athlete1_time - 25

    # Calculate the total race time
    total_time = athlete1_time + athlete2_time + athlete3_time + athlete4_time

    # return the result
    result = total_time
    return result

print(solution())