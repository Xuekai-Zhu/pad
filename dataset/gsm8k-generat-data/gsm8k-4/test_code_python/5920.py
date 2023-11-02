def solution():
    """In a store, there are three types of cheese: white, swiss, and blue cheese. Each cheese is packaged, and there are 200 grams of cheese in each package. The package prices are $5 for white cheese, $6 for swiss cheese, and $8 for blue cheese. Miley needed to get some for her party, and she decided to buy 5 packs of swiss cheese, 600 grams of blue cheese, and one-third less white cheese. How much did she need to pay for all the cheese?"""
    
    # Define the package size and prices for each cheese type
    PACKAGE_SIZE = 200
    WHITE_PRICE = 5
    SWISS_PRICE = 6
    BLUE_PRICE = 8
    
    # Calculate the total amount of cheese purchased (in grams)
    white_cheese = (2/3)*5*PACKAGE_SIZE
    swiss_cheese = 5*PACKAGE_SIZE
    blue_cheese = 600
    
    # Calculate the total cost of each cheese type
    white_cost = white_cheese/PACKAGE_SIZE * WHITE_PRICE
    swiss_cost = swiss_cheese/PACKAGE_SIZE * SWISS_PRICE
    blue_cost = blue_cheese/PACKAGE_SIZE * BLUE_PRICE
    
    # Calculate the total cost of all cheese
    total_cost = white_cost + swiss_cost + blue_cost
    
    # Return the result
    result = total_cost
    return result

print(solution())