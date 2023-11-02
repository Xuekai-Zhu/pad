def solution():
    total_stamps = 100
    chinese_percentage = 0.35
    us_percentage = 0.2

    # Calculate the number of Chinese stamps
    chinese_stamps = total_stamps * chinese_percentage

    # Calculate the number of US stamps
    us_stamps = total_stamps * us_percentage

    # Calculate the number of Japanese stamps
    japanese_stamps = total_stamps - chinese_stamps - us_stamps
    result = japanese_stamps
    return result

print(solution())