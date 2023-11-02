def solution():
    
    total_stamps = 100
    chinese_stamps = total_stamps * 0.35
    us_stamps = total_stamps * 0.2
    japanese_stamps = total_stamps - chinese_stamps - us_stamps
    result = japanese_stamps
    return result

print(solution())