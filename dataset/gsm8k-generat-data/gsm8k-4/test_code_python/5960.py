def solution():
    """Josiah is three times as old as Hans. Hans is 15 years old now. In three years, what is the sum of the ages of Josiah and Hans?"""
    # Define Hans' age
    hans_age = 15

    # Calculate Josiah's age
    josiah_age = hans_age * 3

    # Calculate the sum of their ages in three years
    sum_in_three_years = (hans_age + 3) + (josiah_age + 3)

    result = sum_in_three_years
    return result

print(solution())