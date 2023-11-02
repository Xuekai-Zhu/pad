def solution():
    # Define the year that the Magna Carta was signed and Larry King was born
    magna_carta_year = 1215
    larry_king_birth_year = 1933
    # Check if Larry King could have possibly signed the Magna Carta based on his birth year
    if larry_king_birth_year > magna_carta_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())