def solution():
    """Dane’s two daughters need to plant 5 flowers each to grow a garden. As the days passed, the flowers grew into 20 more but 10 of them died. Dane’s daughters harvested the flowers and split them between 5 different baskets. How many flowers ended up in each basket?"""
    # Define the initial number of flowers
    initial_flowers = 2 * 5

    # Calculate the total number of flowers after growth and death
    total_flowers = initial_flowers + 20 - 10

    # Calculate the number of flowers per basket
    flowers_per_basket = total_flowers / 5

    result = flowers_per_basket
    return result

print(solution())