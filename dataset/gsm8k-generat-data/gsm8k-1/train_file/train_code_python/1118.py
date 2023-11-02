def solution():
    """Jill spends time every day talking to her boyfriend on the phone. The first day of the week she spends 5 minutes on the phone with her boyfriend. Each of the following days she spends twice as much time talking on the phone as the day before. After the 5th day her parents take the phone away from her because she was on it too long. How much time did Jill spend talking to her boyfriend that week?"""
    days = 5
    initial_time = 5
    total_time = 0
    for i in range(days):
        total_time += initial_time
        initial_time *= 2
    result = total_time
    return result

print(solution())