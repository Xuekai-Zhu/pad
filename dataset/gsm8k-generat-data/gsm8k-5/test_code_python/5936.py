def solution():
    total_flour_needed = 9 * 2 * 100  # 2 people baking 9 cakes each, each cake needs 100g of flour
    flour_at_Harris = 400  # Harris has 400g of flour
    flour_from_Traci = total_flour_needed - flour_at_Harris  # Traci brought the remaining flour from her own house
    result = flour_from_Traci
    return result

print(solution())