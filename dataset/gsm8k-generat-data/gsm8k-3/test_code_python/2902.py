def solution():
    """Dane’s two daughters need to plant 5 flowers each to grow a garden. As the days passed, the flowers grew into 20 more but 10 of them died. Dane’s daughters harvested the flowers and split them between 5 different baskets. How many flowers ended up in each basket?"""
    # Define the total number of flowers planted
    total_planted = 2 * 5

    # Calculate the total number of flowers after growth and death
    total_grown = total_planted + 20 - 10

    # Calculate the number of flowers in each basket
    flowers_per_basket = total_grown / 5

    # Display the number of flowers per basket
    result = flowers_per_basket
    return result

print(solution())