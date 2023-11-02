def solution():
    """Akeno spent $2985 to furnish his apartment. Lev spent one-third of that amount on his apartment and Ambrocio spent $177 less than Lev. How many dollars more did Akeno spend than the other 2 people combined?"""
    # Define the amount Akeno spent on furnishing his apartment
    akeno_spent = 2985

    # Define the amount Lev spent on his apartment
    lev_spent = akeno_spent / 3

    # Define the amount Ambrocio spent on his apartment
    ambrocio_spent = lev_spent - 177

    # Calculate the total amount spent by Lev and Ambrocio combined
    lev_ambrocio_total = lev_spent + ambrocio_spent

    # Calculate how much more Akeno spent than Lev and Ambrocio combined
    difference = akeno_spent - lev_ambrocio_total

    result = difference
    return result

print(solution())