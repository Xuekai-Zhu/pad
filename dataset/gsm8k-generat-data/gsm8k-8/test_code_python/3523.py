def solution():
    # Calculate the number of females in the class
    females = 0.6 * 200

    # Calculate the number of female brunettes
    female_brunettes = 0.5 * females

    # Calculate the number of female brunettes under 5 feet tall
    female_brunettes_under_5 = 0.5 * female_brunettes

    result = female_brunettes_under_5
    return result

print(solution())