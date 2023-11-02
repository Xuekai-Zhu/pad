def solution():
    # Find the number of screens sold in February
    february_screens = 2 * january_screens

    # Find the number of screens sold in March
    march_screens = 8800

    # Find the number of screens sold from January to March
    total_screens = january_screens + february_screens + march_screens
    result = total_screens
    return result

print(solution())