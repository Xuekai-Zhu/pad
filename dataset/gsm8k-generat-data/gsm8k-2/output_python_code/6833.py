def solution():
    """Sara sent letters to her friend in China every month. She sent 6 letters in January, 9 letters in February, and in March she sent triple the number of letters she sent in January. How many letters does Sara send?"""
    january_letters = 6
    february_letters = 9
    march_letters = january_letters * 3
    total_letters = january_letters + february_letters + march_letters
    result = total_letters
    return result

print(solution())