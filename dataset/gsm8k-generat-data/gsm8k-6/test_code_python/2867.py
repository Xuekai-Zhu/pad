def solution():
    # Calculate Micah's speed
    micah_speed = (2/3) * (1/9)  # Micah runs 2/3 times as fast as Dean, who takes 9 hours

    # Calculate Jake's time to finish the marathon
    jake_time = (4/3) * (1/micah_speed)  # Jake takes 1/3 times more time to finish the marathon than Micah

    # Calculate the total time for the three to complete the marathon
    total_time = 9 + (1/micah_speed) + jake_time 
    result = total_time
    return result

print(solution())