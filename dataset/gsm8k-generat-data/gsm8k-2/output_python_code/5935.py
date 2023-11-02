def solution():
    """Traci and Harris are baking cakes together. Traci has brought flour from her own house and Harris has 400g of flour in his house. Each cake needs 100g of flour and Traci and Harris have created 9 cakes each. How much flour, in grams, did Traci bring from her own house?"""
    cakes_needed = 18
    flour_in_house = 400
    flour_per_cake = 100
    flour_needed = cakes_needed * flour_per_cake
    flour_brought = flour_needed - flour_in_house
    result = flour_brought
    return result

print(solution())