def solution():
    """Billy and Margaret are competing with each other to see who can swim 10 laps the fastest. Billy swims his first 5 laps in 2 minutes, swims the next 3 laps in 4 minutes, swims the next lap in 1 minute, then swims his final lap. Margaret finishes swimming all of her laps in 10 minutes. Billy wins the competition by finishing his laps 30 seconds before Margaret does. In seconds, how long did it take Billy to swim his final lap?"""
    total_laps = 10
    billy_first_5_time = 2 * 60
    billy_next_3_time = 4 * 60
    billy_next_1_time = 1 * 60
    billy_total_time = billy_first_5_time + billy_next_3_time + billy_next_1_time
    billy_final_lap_time = (10 * 60 - billy_total_time) / 60 + 30  # convert to seconds and add 30 seconds
    result = billy_final_lap_time
    return result

print(solution())