def solution():
    # Calculate Lila's time taken to watch one video
    lila_speed = 2 * 1  # Lila watches at two times the average speed
    lila_time = 100 / lila_speed

    # Calculate Roger's time taken to watch one video
    roger_speed = 1  # Roger watches at the average speed
    roger_time = 100 / roger_speed

    # Calculate the total time they took to watch 6 videos
    total_time = 6 * (lila_time + roger_time)
    result = total_time
    return result

print(solution())