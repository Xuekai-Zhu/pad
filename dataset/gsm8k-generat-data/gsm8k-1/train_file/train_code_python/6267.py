def solution():
    """Maryann spends seven times as long doing accounting as calling clients. If she worked 560 minutes today, how many minutes did she spend calling clients?"""
    total_time = 560
    accounting_time = (7/8) * total_time
    calling_time = total_time - accounting_time
    result = calling_time
    return result

print(solution())