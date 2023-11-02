def solution():
    # Calculate the number of Chinese stamps Nikka has
    chinese_stamps = 0.35 * 100

    # Calculate the number of US stamps Nikka has
    us_stamps = 0.2 * 100

    # Calculate the number of Japanese stamps Nikka has
    japanese_stamps = 100 - chinese_stamps - us_stamps

    result = japanese_stamps
    return result

print(solution())