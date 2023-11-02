def solution():
    
    road_length = 2000
    road_width = 20
    total_area = road_length * road_width
    area_per_truckload = 800
    truckloads_needed = total_area / area_per_truckload
    cost_per_truckload = 75
    sales_tax_rate = 0.2
    total_cost = truckloads_needed * cost_per_truckload * (1 + sales_tax_rate)
    result = total_cost
    return result

print(solution())