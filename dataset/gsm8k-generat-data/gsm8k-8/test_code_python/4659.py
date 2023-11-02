def solution():
    # Calculate the number of female passengers
    female_passengers = 48 * (2/3)

    # Calculate the number of male passengers
    male_passengers = 48 - female_passengers

    # Calculate the number of standing men
    standing_men = male_passengers * (1/8)

    # Calculate the number of seated men
    seated_men = male_passengers - standing_men
    result = seated_men
    return result

print(solution())