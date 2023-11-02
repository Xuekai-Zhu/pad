def solution():
    """Bingley has 5 bracelets. Kelly gives Bingley a fourth of her 16 bracelets. Then Bingley gives a third of his bracelets to his little sister. How many bracelets does Bingley have remaining?"""
    # Initialize the number of Bingley's bracelets
    bingley_bracelets = 5

    # Calculate the number of bracelets Kelly gives to Bingley
    kelly_bracelets = 16 / 4
    bingley_bracelets += kelly_bracelets

    # Calculate the number of bracelets Bingley gives to his little sister
    sister_bracelets = bingley_bracelets / 3
    bingley_bracelets -= sister_bracelets

    # Display the number of bracelets Bingley has remaining
    result = bingley_bracelets
    return result

print(solution())