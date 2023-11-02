def solution():
    """If 3 boys each make 12 muffins for a bake sale, and 2 other girls are making 20 muffins each, how many total muffins will be for sale?"""
    # Define the number of muffins made by each boy and girl
    BOY_MUFFINS = 12
    GIRL_MUFFINS = 20

    # Calculate the total number of muffins made by the boys
    boy_total = 3 * BOY_MUFFINS

    # Calculate the total number of muffins made by the girls
    girl_total = 2 * GIRL_MUFFINS

    # Calculate the total number of muffins for sale
    total_muffins = boy_total + girl_total

    # Display the total number of muffins for sale
    result = total_muffins
    return result

print(solution())