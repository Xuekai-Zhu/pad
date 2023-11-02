def solution():
    packs_sold = 12 + 7 + 5  # Tory has sold a total of 12 + 7 + 5 packs of cookies
    packs_needed = 50  # Tory needs to sell a total of 50 packs of cookies

    # Calculate the packs of cookies Tory still needs to sell
    packs_remaining = packs_needed - packs_sold
    result = packs_remaining
    return result

print(solution())