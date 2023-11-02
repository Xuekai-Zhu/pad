def solution():
    # Number of letters sent in January
    january_letters = 6

    # Number of letters sent in February
    february_letters = 9

    # Number of letters sent in March
    march_letters = january_letters * 3

    # Total number of letters sent
    total_letters = january_letters + february_letters + march_letters
    result = total_letters
    return result

print(solution())