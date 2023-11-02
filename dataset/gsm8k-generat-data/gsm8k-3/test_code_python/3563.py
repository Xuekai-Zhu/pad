def solution():
    """There are 12 bananas and 4 apples in the blue basket. The red basket holds half as many fruits as the blue basket. How many fruits are in the red basket?"""
    # Define the number of fruits in the blue basket
    blue_basket_fruits = 12 + 4

    # Calculate the number of fruits in the red basket
    red_basket_fruits = blue_basket_fruits / 2

    # Display the number of fruits in the red basket
    result = red_basket_fruits
    return result

print(solution())