def solution():
    """In a store, there are three types of cheese: white, swiss, and blue cheese. Each cheese is packaged, and there are 200 grams of cheese in each package. The package prices are $5 for white cheese, $6 for swiss cheese, and $8 for blue cheese. Miley needed to get some for her party, and she decided to buy 5 packs of swiss cheese, 600 grams of blue cheese, and one-third less white cheese. How much did she need to pay for all the cheese?"""
    # Define the weight and price of each type of cheese
    WHITE_WEIGHT = 5 * 200
    SWISS_WEIGHT = 5 * 200
    BLUE_WEIGHT = 600
    WHITE_PRICE = 5
    SWISS_PRICE = 6
    BLUE_PRICE = 8

    # Calculate the weight and price of the white cheese
    white_weight = (2 / 3) * WHITE_WEIGHT
    white_price = white_weight / 200 * WHITE_PRICE

    # Calculate the total weight and price of all the cheese
    total_weight = WHITE_WEIGHT + SWISS_WEIGHT + BLUE_WEIGHT
    total_price = white_price + SWISS_WEIGHT / 200 * SWISS_PRICE + BLUE_WEIGHT / 200 * BLUE_PRICE

    # Display the total price
    result = total_price
    return result

print(solution())