def solution():
    # Tina runs a mile in 6 minutes, which is one-third as fast as Tom
    tom_time = 6 / (1/3)  # Tom's mile time is 18 minutes
    # Tony runs a mile twice as fast as Tina
    tina_time = 6
    tony_time = tina_time / 2
    # Calculate the total time for all three runners
    total_time = tina_time + tony_time + tom_time
    result = total_time
    return result

print(solution())