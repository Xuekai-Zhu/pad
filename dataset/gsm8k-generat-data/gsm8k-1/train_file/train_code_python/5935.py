def solution():
    """Traci and Harris are baking cakes together. Traci has brought flour from her own house and Harris has 400g of flour in his house. Each cake needs 100g of flour and Traci and Harris have created 9 cakes each. How much flour, in grams, did Traci bring from her own house?"""
    total_cakes = 9
    flour_per_cake = 100
    total_flour = 400 + (total_cakes * flour_per_cake * 2)
    flour_from_traci = total_flour/2
    result = flour_from_traci
    return result

print(solution())