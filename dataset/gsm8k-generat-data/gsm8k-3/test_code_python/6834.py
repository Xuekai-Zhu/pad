def solution():
    """Sara sent letters to her friend in China every month. She sent 6 letters in January, 9 letters in February, and in March she sent triple the number of letters she sent in January. How many letters does Sara send?"""
    # Define the number of letters sent in each month
    jan_letters = 6
    feb_letters = 9
    mar_letters = jan_letters * 3

    # Calculate the total number of letters sent
    total_letters = jan_letters + feb_letters + mar_letters

    # Display the total number of letters sent
    result = total_letters
    return result

print(solution())