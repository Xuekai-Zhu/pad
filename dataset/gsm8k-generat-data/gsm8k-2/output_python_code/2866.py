def solution():
    """Micah, Dean, and Jake are all training for a marathon organized by a local NGO to support children in their town who have cancer. Micah runs 2/3 times as fast as Dean. It takes Jake 1/3 times more time to finish the marathon than it takes Mica. If Dean takes 9 hours, what's the total time the three take to complete the marathon?"""
    dean_time = 9
    micah_time = (2/3) * dean_time
    jake_time = (4/3) * micah_time
    total_time = dean_time + micah_time + jake_time
    result = total_time
    return result

print(solution())