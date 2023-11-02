def solution():
    brother_letters = 40   # Greta's brother received 40 letters
    greta_letters = brother_letters + 10   # Greta received 10 more letters than her brother
    total_letters = brother_letters + greta_letters   # Total number of letters received by Greta and her brother
    mother_letters = 2 * total_letters   # Greta's mother received twice the total number of letters

    # Calculate the total number of letters the three received
    total = mother_letters + total_letters
    result = total
    return result

print(solution())