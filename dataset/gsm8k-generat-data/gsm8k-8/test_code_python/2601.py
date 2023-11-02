def solution():
    # Calculate James' earnings in February
    february_earnings = 2 * 4000

    # Calculate James' earnings in March
    march_earnings = february_earnings - 2000

    # Calculate James' total earnings so far this year
    total_earnings = 4000 + february_earnings + march_earnings

    result = total_earnings
    return result

print(solution())