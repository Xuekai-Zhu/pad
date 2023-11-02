def solution():
    """Sara sent letters to her friend in China every month. She sent 6 letters in January, 9 letters in February, and in March she sent triple the number of letters she sent in January. How many letters does Sara send?"""
    jan_letters = 6
    feb_letters = 9
    mar_letters = 3 * jan_letters
    total_letters = jan_letters + feb_letters + mar_letters
    result = total_letters
    return result

print(solution())