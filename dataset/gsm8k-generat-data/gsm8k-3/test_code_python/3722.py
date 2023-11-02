def solution():
    """Jorge is 24 years younger than Simon. In 2005, Jorge is 16 years old. In 2010, how old would Simon be?"""
    # Calculate Simon's age in 2005
    jorge_age_2005 = 16
    simon_age_2005 = jorge_age_2005 + 24

    # Calculate Simon's age in 2010
    simon_age_2010 = simon_age_2005 + (2010 - 2005)

    # Display Simon's age in 2010
    result = simon_age_2010
    return result

print(solution())