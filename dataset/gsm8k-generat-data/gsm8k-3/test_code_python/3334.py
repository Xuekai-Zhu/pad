def solution():
    """On his farm, Mr. Mathews has goats and sheep in the ratio of 5:7. He decides to sell half of the goats at $40 each and 2/3 of the sheep at $30 each. How much money does he make from the sale of the animals if the total number of sheep and goats on the farm is 360?"""
    # Define the ratio of goats to sheep
    ratio = 5/7

    # Calculate the number of goats and sheep on the farm
    total_animals = 360
    goats = int(total_animals / (1 + ratio))
    sheep = total_animals - goats

    # Calculate the amount made from selling the goats
    goat_sale = goats/2 * 40

    # Calculate the amount made from selling the sheep
    sheep_sale = (2/3 * sheep) * 30

    # Calculate the total amount made from selling the animals
    total_sale = goat_sale + sheep_sale

    # Display the total amount made
    result = total_sale
    return result

print(solution())