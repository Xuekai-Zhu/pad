def solution():
    """Jermaine, Terrence, and Emilee earn a total of $90. Jermaine earns $5 more than Terrence in a month. If Terrence earns $30, how much does Emilee earn?"""
    # Define Terrence's earnings
    terrence_earnings = 30

    # Calculate Jermaine's earnings
    jermaine_earnings = terrence_earnings + 5

    # Calculate Emilee's earnings
    emilee_earnings = 90 - terrence_earnings - jermaine_earnings

    # Display Emilee's earnings
    result = emilee_earnings
    return result

print(solution())