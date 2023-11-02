def solution():
    """A shop sells laptops at $600 each and a smartphone at $400. Celine buys two laptops and four smartphones for her children. How much change does she get back if she has $3000?"""
    num_laptops = 2
    laptop_cost = 600
    num_smartphones = 4
    smartphone_cost = 400
    total_cost = (num_laptops * laptop_cost) + (num_smartphones * smartphone_cost)
    change = 3000 - total_cost
    result = change
    
    return result

print(solution())