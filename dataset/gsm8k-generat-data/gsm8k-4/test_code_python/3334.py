def solution():
    """On his farm, Mr. Mathews has goats and sheep in the ratio of 5:7. He decides to sell half of the goats at $40 each and 2/3 of the sheep at $30 each. How much money does he make from the sale of the animals if the total number of sheep and goats on the farm is 360?"""
    # Define the ratio of goats to sheep
    ratio = 5/7

    # Calculate the number of goats and sheep respectively
    goats = 5/12 * 360  # 5/12 of the total animals
    sheep = 7/12 * 360  # 7/12 of the total animals

    # Calculate the number of goats to sell and the number of sheep to sell
    goats_to_sell = goats/2
    sheep_to_sell = 2/3 * sheep

    # Calculate the total money earned from selling goats and sheep
    goat_money = goats_to_sell * 40
    sheep_money = sheep_to_sell * 30
    total_money = goat_money + sheep_money

    result = total_money
    return result

print(solution())