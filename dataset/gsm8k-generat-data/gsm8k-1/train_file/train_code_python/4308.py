def solution():
    """Mark is buying asphalt to pave a new section of road. The road will be 2000 feet long and 20 feet wide. Each truckload of asphalt will cover 800 square feet of road. If each truckload costs $75, and there's a 20% sales tax, how much will Mark need to pay for asphalt?"""
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