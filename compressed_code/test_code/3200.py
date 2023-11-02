def solution():
    
    kenneth_fabric = 700
    kenneth_price_per_oz = 40
    kenneth_total_price = kenneth_fabric * kenneth_price_per_oz
    nicholas_fabric = kenneth_fabric * 6
    nicholas_price_per_oz = kenneth_price_per_oz
    nicholas_total_price = nicholas_fabric * nicholas_price_per_oz
    difference = nicholas_total_price - kenneth_total_price
    result = difference
    return result

print(solution())