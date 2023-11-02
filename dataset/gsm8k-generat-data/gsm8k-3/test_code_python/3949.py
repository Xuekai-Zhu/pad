def solution():
    """Nikka has a 100 stamp collection. Thirty-five percent of her stamps are Chinese, 20% are US stamps, and the rest are Japanese stamps. How many Japanese stamps does Nikka have?"""
    # Define the total number of stamps
    total_stamps = 100

    # Calculate the number of Chinese stamps
    chinese_stamps = total_stamps * 0.35

    # Calculate the number of US stamps
    us_stamps = total_stamps * 0.2

    # Calculate the number of Japanese stamps
    japanese_stamps = total_stamps - chinese_stamps - us_stamps

    # Display the number of Japanese stamps
    result = japanese_stamps
    return result

print(solution())