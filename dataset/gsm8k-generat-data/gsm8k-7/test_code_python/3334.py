def solution():
    # Define ratio
    goat_to_sheep_ratio = 5/7

    # Calculate number of goats and sheep
    total_animals = 360
    num_sheep = total_animals * goat_to_sheep_ratio * (7/12)
    num_goats = total_animals * goat_to_sheep_ratio * (5/12)

    # Calculate amount made from selling goats
    num_goats_sold = num_goats / 2
    goats_sale_price = 40
    total_goats_sale_amount = num_goats_sold * goats_sale_price

    # Calculate amount made from selling sheep
    num_sheep_sold = (2/3) * num_sheep
    sheep_sale_price = 30
    total_sheep_sale_amount = num_sheep_sold * sheep_sale_price

    # Calculate total money made from sale of animals
    total_sale_amount = total_goats_sale_amount + total_sheep_sale_amount
    result = total_sale_amount
    return result

print(solution())