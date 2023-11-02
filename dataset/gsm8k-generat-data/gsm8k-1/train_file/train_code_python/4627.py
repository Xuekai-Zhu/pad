def solution():
    """Greta received 10 more letters in the mail than her brother. Greta's mother received twice the total number of letters Greta and her brother received. Calculate the total number of letters the three received if Greta's brother received 40 letters."""
    brother_letters = 40
    greta_letters = brother_letters + 10
    total_letters = brother_letters + greta_letters
    mother_letters = total_letters * 2
    total_letters_received = total_letters + mother_letters
    result = total_letters_received
    
    return result

print(solution())