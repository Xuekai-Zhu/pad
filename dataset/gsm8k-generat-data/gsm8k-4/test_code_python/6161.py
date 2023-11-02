def solution():
    """Jermaine, Terrence, and Emilee earn a total of $90. Jermaine earns $5 more than Terrence in a month. If Terrence earns $30, how much does Emilee earn?"""
    # Define Terrence's earnings
    terrence_earnings = 30

    # Define Jermaine's earnings as Terrence's earnings plus $5
    jermaine_earnings = terrence_earnings + 5

    # Calculate the total earnings of all three
    total_earnings = jermaine_earnings + terrence_earnings + emilee_earnings

    # Calculate Emilee's earnings by subtracting Terrence's and Jermaine's earnings from the total
    emilee_earnings = total_earnings - jermaine_earnings - terrence_earnings

    # return the result
    result = emilee_earnings
    return result

print(solution())