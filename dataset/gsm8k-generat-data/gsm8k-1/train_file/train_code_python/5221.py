def solution():
    """Jim decides to buy mayo in bulk. He can buy 1 gallon of mayo at Costco for 8 dollars. At the normal store, a 16-ounce bottle costs $3. How much money does he save by buying the gallon container?"""
    costco_price = 8
    normal_store_price = 3
    normal_store_size = 16 # in ounces
    gallon_size = 128 # in ounces
    costco_price_per_ounce = costco_price / gallon_size
    normal_store_price_per_ounce = normal_store_price / normal_store_size
    savings_per_ounce = normal_store_price_per_ounce - costco_price_per_ounce
    savings_per_gallon = savings_per_ounce * gallon_size
    result = savings_per_gallon
    return result

print(solution())