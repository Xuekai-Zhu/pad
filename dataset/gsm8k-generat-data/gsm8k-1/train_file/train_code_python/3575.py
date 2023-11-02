def solution():
    """Billy and Margaret are competing with each other to see who can swim 10 laps the fastest. Billy swims his first 5 laps in 2 minutes, swims the next 3 laps in 4 minutes, swims the next lap in 1 minute, then swims his final lap. Margaret finishes swimming all of her laps in 10 minutes. Billy wins the competition by finishing his laps 30 seconds before Margaret does. In seconds, how long did it take Billy to swim his final lap?"""
    total_time_billy = 2*5 + 3*4 + 1
    total_time_margaret = 10*60
    final_time_billy = (total_time_billy - total_time_margaret + 30) / 60
    final_lap_time_billy = final_time_billy - 2*5 - 3*4 - 1
    result = final_lap_time_billy * 60
    return result

print(solution())