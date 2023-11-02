def solution():
    """Greta received 10 more letters in the mail than her brother. Greta's mother received twice the total number of letters Greta and her brother received. Calculate the total number of letters the three received if Greta's brother received 40 letters."""
    # Define the number of letters received by Greta's brother
    brother_letters = 40

    # Calculate the number of letters received by Greta
    greta_letters = brother_letters + 10

    # Calculate the total number of letters received by Greta and her brother
    total_letters = brother_letters + greta_letters

    # Calculate the number of letters received by Greta's mother
    mother_letters = 2 * total_letters

    # Calculate the total number of letters received by the three
    total = brother_letters + greta_letters + mother_letters

    result = total
    return result

print(solution())