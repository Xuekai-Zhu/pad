def solution():
    """Akeno spent $2985 to furnish his apartment. Lev spent one-third of that amount on his apartment and Ambrocio spent $177 less than Lev. How many dollars more did Akeno spend than the other 2 people combined?"""
    # Define the total amount spent by Akeno
    AKENO_SPENT = 2985

    # Calculate the amount spent by Lev
    LEV_SPENT = AKENO_SPENT / 3

    # Calculate the amount spent by Ambrocio
    AMBROCIO_SPENT = LEV_SPENT - 177

    # Calculate the total amount spent by Lev and Ambrocio combined
    LEV_AMBROCIO_SPENT = LEV_SPENT + AMBROCIO_SPENT

    # Calculate the amount Akeno spent more than Lev and Ambrocio combined
    amount_more_spent = AKENO_SPENT - LEV_AMBROCIO_SPENT

    # Display the amount Akeno spent more than Lev and Ambrocio combined
    result = amount_more_spent
    return result

print(solution())