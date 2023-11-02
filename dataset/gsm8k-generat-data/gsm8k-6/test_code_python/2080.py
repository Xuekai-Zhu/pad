def solution():
    # Calculate the total earnings per day
    total_normal = 5 * 5  # 5 normal haircuts charged at $5 each
    total_special = 3 * 6  # 3 special haircuts charged at $6 each
    total_trendy = 2 * 8  # 2 trendy haircuts charged at $8 each
    total_earnings = total_normal + total_special + total_trendy

    # Calculate the total earnings per week
    earnings_per_week = total_earnings * 7  # assuming the hairstylist works 7 days a week
    result = earnings_per_week
    return result

print(solution())