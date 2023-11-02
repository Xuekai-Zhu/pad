def solution():
    # Calculate the number of female students in the class
    females = 0.6 * 200  # 60% of the students were female

    # Calculate the number of female brunettes in the class
    brunette_females = 0.5 * females  # 50% of the females were brunettes

    # Calculate the number of female brunettes under 5 feet tall
    short_brunettes = 0.5 * brunette_females  # 50% of the female brunettes were under 5 feet tall

    result = short_brunettes
    return result

print(solution())