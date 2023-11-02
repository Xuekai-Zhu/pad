def solution():
    """Hannah comes home from work to find her older son taped her younger son to a chair with 22 strands of duct tape. If Hannah can cut 8 strands per minute and her son can cut 3 strands per minute, how long will it take them to free her younger son?"""
    tape_strands = 22
    hannah_rate = 8
    son_rate = 3
    total_rate = hannah_rate + son_rate
    time_to_free = tape_strands / total_rate
    result = time_to_free
    return result

print(solution())