def solution():
    
    square_meters = 20
    trees_per_square_meter = 2
    coconuts_per_tree = 6
    harvest_interval_in_months = 3
    coconuts_per_harvest = square_meters * trees_per_square_meter * coconuts_per_tree
    total_harvests = 6 // harvest_interval_in_months
    total_coconuts_harvested = coconuts_per_harvest * total_harvests
    price_per_coconut = 0.50
    total_earnings = total_coconuts_harvested * price_per_coconut
    result = total_earnings
    return result

print(solution())