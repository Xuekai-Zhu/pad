def solution():
    # Define the number of cows and pigs
    cows = 20
    pigs = 4 * cows

    # Define the prices per cow and per pig
    cow_price = 800
    pig_price = 400

    # Calculate the total earnings from selling all animals
    total_earnings = (cows * cow_price) + (pigs * pig_price)
    result = total_earnings
    return result

print(solution())