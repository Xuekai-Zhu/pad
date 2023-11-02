def solution():
    """Maryann spends seven times as long doing accounting as calling clients. If she worked 560 minutes today, how many minutes did she spend calling clients?"""
    total_time = 560
    accounting_time = 7 * calling_time
    calling_time = total_time / 8
    result = calling_time
    return result

print(solution())