def solution():
    # Calculate total stopping time
    stopping_time = (14 // 2 + 2 + 3) * 20 / 60  # 14 // 2 gives the number of stops, and additional stops are added. 20/60 converts minutes to hours.

    # Calculate the total time of the road trip including stopping time
    total_time = 14 + stopping_time
    result = total_time
    return result

print(solution())