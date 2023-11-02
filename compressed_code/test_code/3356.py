def solution():
    
    road_length = 2000
    road_width = 20
    area_per_truckload = 800
    num_truckloads = (road_length * road_width) / area_per_truckload
    truckload_cost = 75
    subtotal = num_truckloads * truckload_cost
    sales_tax_rate = 0.2
    sales_tax = sales_tax_rate * subtotal
    total_cost = subtotal + sales_tax
    result = total_cost
    return result

print(solution())