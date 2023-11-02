def solution():
    total_stamps = 100  # Nikka has a 100 stamp collection
    chinese_stamps = int(0.35 * total_stamps)  # 35% of stamps are Chinese
    us_stamps = int(0.2 * total_stamps)  # 20% of stamps are US
    japanese_stamps = total_stamps - chinese_stamps - us_stamps  # The rest are Japanese stamps
    result = japanese_stamps
    return result

print(solution())