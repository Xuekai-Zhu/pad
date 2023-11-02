def solution():
    """Javier spends 30 minutes outlining his speech, 28 more minutes writing than outlining, and half as much time practicing as writing. How much time does he spend on his speech in total?"""
    outlining_time = 30
    writing_time = outlining_time + 28
    practicing_time = writing_time / 2
    total_time = outlining_time + writing_time + practicing_time
    result = total_time
    return result

print(solution())