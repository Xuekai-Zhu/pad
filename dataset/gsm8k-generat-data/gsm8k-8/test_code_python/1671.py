def solution():
    # Define the initial width of the river
    initial_width = 50

    # Define the rate of increase in width per meter
    increase_rate = 2/10

    # Define the target width
    target_width = 80

    # Calculate the distance they need to row along the river
    distance = (target_width - initial_width) / increase_rate

    # Calculate the time it will take them to row the distance
    time = distance / 5

    result = time
    return result

print(solution())