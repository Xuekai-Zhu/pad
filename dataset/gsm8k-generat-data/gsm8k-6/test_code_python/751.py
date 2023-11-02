def solution():
    # Calculate the speed of Harry on Monday and Tuesday-Thursday
    speed_Monday = 10  # meters per hour
    speed_Tue_Thu = 1.5 * speed_Monday  # 50% faster than on Monday

    # Calculate the speed of Harry on Friday
    speed_Friday = 1.6 * speed_Tue_Thu  # 60% faster than on Thursday

    result = speed_Friday
    return result

print(solution())