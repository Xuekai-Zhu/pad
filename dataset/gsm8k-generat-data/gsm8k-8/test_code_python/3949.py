def solution():
    # Define the number of Chinese and US stamps
    chinese_stamps = 0.35 * 100
    us_stamps = 0.2 * 100

    # Calculate the number of Japanese stamps
    japanese_stamps = 100 - chinese_stamps - us_stamps
    result = japanese_stamps
    return result

print(solution())