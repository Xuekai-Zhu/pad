def solution():
    total_earnings = 90
    terrence_earnings = 30
    jermaine_earnings = terrence_earnings + 5

    # Calculate Emilee's earnings
    emilee_earnings = total_earnings - terrence_earnings - jermaine_earnings
    result = emilee_earnings
    return result

print(solution())