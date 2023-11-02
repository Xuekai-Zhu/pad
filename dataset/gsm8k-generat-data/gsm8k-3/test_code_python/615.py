def solution():
    """Connie is trying to remember when her grandmother was born. She knows her grandmother's older brother was born in 1932, her older sister was born in 1936, and the gap between her grandmother and her sister is twice the gap between the older brother and the older sister. What year was Connie's grandma born?"""
    # Define the year when the older brother was born
    older_brother_birthyear = 1932

    # Define the year when the older sister was born
    older_sister_birthyear = 1936

    # Calculate the gap between the older brother and the older sister
    brother_sister_gap = older_sister_birthyear - older_brother_birthyear

    # Calculate the gap between the grandmother and the older sister
    grandma_sister_gap = brother_sister_gap * 2

    # Calculate the year when the grandmother was born
    grandma_birthyear = older_sister_birthyear + grandma_sister_gap

    # Display the year when the grandmother was born
    result = grandma_birthyear
    return result

print(solution())