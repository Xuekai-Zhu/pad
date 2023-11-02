def solution():
     square_meters = 20
     trees_per_square_meter = 2
     coconuts_per_tree = 6
     coconuts_harvested = square_meters * trees_per_square_meter * coconuts_per_tree
     cost_per_coconut = 0.50
     total_cost = coconuts_harvested * cost_per_coconut
     result = total_cost
     return result

print(solution())