def solution():
    """Trevor's older brother was twice his age 20 years ago. How old was Trevor a decade ago if his brother is now 32 years old?"""
    # Define Trevor's brother's current age
    brother_age = 32

    # Calculate Trevor's age 20 years ago
    trevor_20_years_ago = (brother_age / 2) - 20

    # Calculate Trevor's age a decade ago
    trevor_10_years_ago = trevor_20_years_ago + 10

    # Display Trevor's age a decade ago
    result = trevor_10_years_ago
    return result

print(solution())