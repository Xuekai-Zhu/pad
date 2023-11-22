def solution():
    
    # Define the price of a small stuffed animal and the number of large stuffed animals sold
    SMALL_PRICE = 4
    LARGE_ANIMALS_SOLD = 3

    # Define the total earnings from the sales
    total_earnings = 120

    # Calculate the total number of small stuffed animals sold
    small_animal_sold = (total_earnings / (SMALL_PRICE * LARGE_ANIMALS_SOLD)) * LARGE_ANIMALS_SOLD

    # Display the number of small stuffed animals sold
    result = small_animal_sold
    return result

print(solution())