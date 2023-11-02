def solution():
    """Bingley has 5 bracelets. Kelly gives Bingley a fourth of her 16 bracelets. Then Bingley gives a third of his bracelets to his little sister. How many bracelets does Bingley have remaining?"""
    # Define the initial number of bracelets
    initial_bracelets = 5

    # Calculate the number of bracelets given to Bingley by Kelly
    kelly_bracelets = 16 / 4
    total_bracelets = initial_bracelets + kelly_bracelets

    # Calculate the number of bracelets given to Bingley's little sister
    bingley_bracelets = total_bracelets / 3

    # Calculate the number of bracelets remaining with Bingley
    remaining_bracelets = total_bracelets - bingley_bracelets

    # return the result
    result = remaining_bracelets
    return result

print(solution())