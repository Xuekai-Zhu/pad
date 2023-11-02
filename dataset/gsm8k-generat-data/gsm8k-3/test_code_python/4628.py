def solution():
    """Greta received 10 more letters in the mail than her brother. Greta's mother received twice the total number of letters Greta and her brother received. Calculate the total number of letters the three received if Greta's brother received 40 letters."""
    # Define the number of letters Greta's brother received
    brother_letters = 40

    # Calculate the number of letters Greta received
    greta_letters = brother_letters + 10

    # Calculate the total number of letters Greta and her brother received
    total_letters = greta_letters + brother_letters

    # Calculate the number of letters Greta's mother received
    mother_letters = 2 * total_letters

    # Calculate the total number of letters the three received
    total = total_letters + mother_letters

    # Display the total number of letters
    result = total
    return result

print(solution())