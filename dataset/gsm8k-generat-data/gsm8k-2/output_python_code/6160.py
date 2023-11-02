def solution():
    """Jermaine, Terrence, and Emilee earn a total of $90. Jermaine earns $5 more than Terrence in a month. If Terrence earns $30, how much does Emilee earn?"""
    terrence_earnings = 30
    jermaine_earnings = terrence_earnings + 5
    total_earnings = 90
    emilee_earnings = total_earnings - terrence_earnings - jermaine_earnings
    result = emilee_earnings
    return result

print(solution())