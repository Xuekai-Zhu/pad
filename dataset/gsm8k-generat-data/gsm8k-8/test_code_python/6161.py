def solution():
    # Define Terrence's earnings
    terrence_earnings = 30

    # Calculate Jermaine's earnings
    jermaine_earnings = terrence_earnings + 5

    # Calculate the total earnings of Jermaine and Terrence
    total_jermaine_terrence_earnings = jermaine_earnings + terrence_earnings

    # Calculate Emilee's earnings
    emilee_earnings = 90 - total_jermaine_terrence_earnings
    result = emilee_earnings
    return result

print(solution())