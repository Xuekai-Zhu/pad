def solution():
    distance = 1000  # The distance to the vacation destination is 1000 miles

    # Calculate the time Abel takes to cover the distance
    time_abel = distance / 50  # Abel drives at a speed of 50 miles per hour

    # Calculate the time Alice takes to cover the distance
    time_alice = (distance / 40) - 1  # Alice starts 1 hour after Abel and drives at a speed of 40 miles per hour

    # Calculate the time difference in minutes
    time_difference = (time_abel - time_alice) * 60

    result = time_difference
    return result

print(solution())