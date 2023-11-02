def solution():
    """John decides to do several activities while out on vacation. He spends 6 hours boating and half that time swimming. 
    He also watched 3 different shows which were 2 hours each. This was 30% of the time he spent. He spent 40% of his time sightseeing. 
    How much time did he spend sightseeing?"""
    boating_time = 6
    swimming_time = boating_time / 2
    total_activity_time = boating_time + swimming_time + 6
    show_time = 3 * 2
    show_percent = 30
    total_time = (total_activity_time + show_time) / (100 - show_percent) * 100
    sightseeing_percent = 40
    sightseeing_time = total_time * (sightseeing_percent / 100)
    result = sightseeing_time
    
    return result

print(solution())