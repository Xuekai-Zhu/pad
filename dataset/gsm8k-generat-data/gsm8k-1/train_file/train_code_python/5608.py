def solution():
    """John plays a game for 4 hours a day every day for 2 weeks. After all that time, he is only 40% done. He increased his playtime to 7 hours a day. How long until he finishes the game?"""
    daily_playtime_first = 4
    days_first = 14
    percent_done_first = 40
    daily_playtime_second = 7
    
    total_time = (100/percent_done_first) * daily_playtime_first * days_first
    remaining_time = total_time - (daily_playtime_first * days_first)

    time_to_finish = remaining_time / daily_playtime_second
    result = time_to_finish

    return result

print(solution())