def solution():
    """Javier spends 30 minutes outlining his speech, 28 more minutes writing than outlining, and half as much time practicing as writing. How much time does he spend on his speech in total?"""
    outline_time = 30
    writing_time = outline_time + 28
    practice_time = writing_time / 2
    total_time = outline_time + writing_time + practice_time
    result = total_time
    return result

print(solution())