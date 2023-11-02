def solution():
    """Aida has twice as many dolls as Sophie, and Sophie has twice as many dolls as Vera. How many dolls do Aida, Sophie, and Vera have combined if Vera has 20 dolls?"""
    # Define the number of dolls Vera has
    vera_dolls = 20

    # Calculate the number of dolls Sophie has
    sophie_dolls = vera_dolls * 2

    # Calculate the number of dolls Aida has
    aida_dolls = sophie_dolls * 2

    # Calculate the total number of dolls they have combined
    total_dolls = vera_dolls + sophie_dolls + aida_dolls

    # return the result
    result = total_dolls
    return result

print(solution())