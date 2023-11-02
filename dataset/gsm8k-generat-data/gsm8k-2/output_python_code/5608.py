def solution():
    """John plays a game for 4 hours a day every day for 2 weeks. After all that time, he is only 40% done. He increased his playtime to 7 hours a day. How long until he finishes the game?"""
    total_time = 14 * 4  # 2 weeks * 7 days/week * 4 hours/day
    progress = 0.4
    remaining_progress = 1 - progress
    remaining_time = (remaining_progress * total_time) / 7  # 7 hours/day after increasing playtime
    result = remaining_time
    return result

print(solution())