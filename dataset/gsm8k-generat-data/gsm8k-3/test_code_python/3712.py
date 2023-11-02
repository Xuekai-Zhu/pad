def solution():
    """Peter is raking leaves. It takes him 15 minutes to rake 3 bags of leaves. If he keeps raking at the same rate, how long will it take him to rake 8 bags?"""
    # Define the rate of raking in bags per minute
    RATE = 3 / 15

    # Calculate the time it would take to rake 8 bags at the same rate
    time = 8 / RATE

    # Convert the time to minutes
    time *= 60

    # Display the time it would take to rake 8 bags
    result = time
    return result

print(solution())