def solution():
    """Nikka has a 100 stamp collection. Thirty-five percent of her stamps are Chinese, 20% are US stamps, and the rest are Japanese stamps. How many Japanese stamps does Nikka have?"""
    total_stamps = 100
    chinese_stamps = total_stamps * 0.35
    us_stamps = total_stamps * 0.2
    japanese_stamps = total_stamps - chinese_stamps - us_stamps
    result = japanese_stamps
    return result

print(solution())