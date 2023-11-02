def solution():
    """Greg has an alarm set to ring three times a day as a reminder. When the alarm goes off, it continues to ring until Greg turns it off. The first time it went off today, it rang four times. The second time it went off, it rang for three times as long as the first time. The third time, it rang for half as long as the second time. How many times did the alarm ring in all?"""
    first_time = 4
    second_time = first_time * 3
    third_time = second_time // 2
    total_rings = first_time + second_time + third_time
    result = total_rings
    return result

print(solution())