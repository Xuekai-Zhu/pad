def solution():
    biology_time = 20  # Max spent 20 minutes on biology
    history_time = 2 * biology_time  # Max spent twice the time on history compared to biology
    geography_time = 3 * history_time  # Max spent three times the time on geography compared to history

    total_time = biology_time + history_time + geography_time
    result = total_time
    return result

print(solution())