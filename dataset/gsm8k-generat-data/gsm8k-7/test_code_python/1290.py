def solution():
    green_ratio = 2  # 2 parts green paint for every 1 part blue and 5 parts white
    green_paint = 6
    total_ratio = green_ratio * 3  # Total ratio is 1 + 2 + 5 = 8 parts
    total_paint = (green_paint / green_ratio) * total_ratio
    result = total_paint
    return result

print(solution())