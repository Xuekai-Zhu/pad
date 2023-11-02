def solution():
    """Marcy makes homemade candles that she markets as 99% guaranteed not to explode. 5% of the more dangerous candles also have a defect that makes them smell like wet dog. If she makes 50000 candles, how many of them will both smell like wet dog and explode?"""
    total_candles = 50000
    danger_percent = 1 - 0.99  # 1% of candles are more dangerous
    defect_percent = 0.05  # of those, 5% have a wet dog smell defect
    danger_candles = total_candles * danger_percent
    wetdog_candles = danger_candles * defect_percent
    exploded_and_wetdog_candles = wetdog_candles  # all wetdog candles are also more dangerous and could explode
    result = exploded_and_wetdog_candles
    return result

print(solution())