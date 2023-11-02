def solution():
    """Josie grows grapes on her 10-acre farm. Each acre produces 5 tons of grapes per year, and each ton of grapes makes 2 barrels of wine. How many barrels of wine does her farm produce per year?"""
    acres = 10
    tons_per_acre = 5
    barrels_per_ton = 2
    total_tons = acres * tons_per_acre
    total_barrels = total_tons * barrels_per_ton
    result = total_barrels
    return result

print(solution())