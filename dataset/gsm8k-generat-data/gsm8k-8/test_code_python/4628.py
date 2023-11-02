def solution():
    # Determine Greta's number of letters
    greta_letters = 40 + 10

    # Determine the total number of letters
    total_letters = greta_letters + 40

    # Determine Greta's mother's number of letters
    mom_letters = 2 * total_letters

    # Calculate the total number of letters between the three of them
    total = greta_letters + 40 + mom_letters
    result = total
    return result

print(solution())