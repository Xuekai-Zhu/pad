def solution():
    billy_total_time = 0
    billy_total_time += 2*60  # Billy's first 5 laps take 2 minutes (120 seconds)
    billy_total_time += 4*60  # Billy's next 3 laps take 4 minutes (240 seconds)
    billy_total_time += 1*60  # Billy's 9th lap takes 1 minute (60 seconds)
    billy_total_time += 30     # Billy finishes 30 seconds before Margaret

    # Subtract the total time for Billy's first 9 laps to get the time for his final lap
    billy_final_lap_time = billy_total_time - (2*60 + 4*60 + 1*60)

    # Convert the final lap time to seconds
    billy_final_lap_time_seconds = billy_final_lap_time % 60

    result = billy_final_lap_time_seconds
    return result

print(solution())