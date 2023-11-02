def solution():
    """David swims the 100-meter freestyle in 48 seconds.  He swims the 100-meter backstroke 4 seconds slower than he swims the 100-meter freestyle, he swims the 100-meter butterfly 3 seconds slower than he swims the 100-meter backstroke, and he swims the 100-meter breaststroke 2 seconds slower than he swims the 100-meter butterfly.  What is the combined length of time, in seconds, it would take for him to swim all four 100-meter events (the freestyle, the backstroke, the butterfly, and the breaststroke)?"""
    # Define the time it takes for David to swim the freestyle
    freestyle_time = 48

    # Define the time it takes for David to swim the backstroke
    backstroke_time = freestyle_time + 4

    # Define the time it takes for David to swim the butterfly
    butterfly_time = backstroke_time + 3

    # Define the time it takes for David to swim the breaststroke
    breaststroke_time = butterfly_time + 2

    # Calculate the total time it would take for David to swim all four events
    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time

    # Display the total time
    result = total_time
    return result

print(solution())