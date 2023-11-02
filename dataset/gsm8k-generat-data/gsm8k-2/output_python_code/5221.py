def solution():
    """Jim decides to buy mayo in bulk. He can buy 1 gallon of mayo at Costco for 8 dollars. At the normal store, a 16-ounce bottle costs $3. How much money does he save by buying the gallon container?"""
    gallon_cost = 8
    gallon_size = 128  # in ounces
    normal_cost_per_ounce = 3 / 16
    normal_cost_for_gallon = normal_cost_per_ounce * gallon_size
    savings = normal_cost_for_gallon - gallon_cost
    result = savings
    return result

print(solution())