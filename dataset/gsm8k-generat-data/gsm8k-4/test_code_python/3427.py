def solution():
    """In four years, Annika will be three times as old as Hans. If Hans is now 8 years old, how old is Annika now?"""
    # Define Hans's age now
    hans_age = 8

    # Calculate Annika's age in four years
    annika_age_in_four_years = 3 * (hans_age + 4)

    # Calculate Annika's current age
    annika_age = annika_age_in_four_years - 4

    result = annika_age
    return result

print(solution())