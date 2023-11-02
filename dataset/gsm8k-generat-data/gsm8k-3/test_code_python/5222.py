def solution():
    """Jim decides to buy mayo in bulk.  He can buy 1 gallon of mayo at Costco for 8 dollars.  At the normal store, a 16-ounce bottle costs $3.  How much money does he save by buying the gallon container?"""
    # Define the cost of 1 gallon and 16 ounces of mayo
    GALLON_PRICE = 8
    SMALL_PRICE = 3
    SMALL_SIZE = 16
    
    # Calculate the equivalent price of 1 gallon in 16 ounce bottles
    GALLON_SIZE = 128
    gallon_in_small = GALLON_SIZE / SMALL_SIZE
    equivalent_price = GALLON_PRICE / gallon_in_small
    
    # Calculate the cost of buying the same quantity of mayo in 16-ounce bottles
    small_quantity = GALLON_SIZE / SMALL_SIZE
    total_cost = small_quantity * SMALL_PRICE
    
    # Calculate the savings from buying in bulk
    savings = total_cost - GALLON_PRICE
    
    # Display the savings
    result = savings
    return result

print(solution())