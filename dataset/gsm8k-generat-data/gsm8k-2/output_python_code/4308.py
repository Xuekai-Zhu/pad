def solution():
    """Mark is buying asphalt to pave a new section of road. The road will be 2000 feet long and 20 feet wide. Each truckload of asphalt will cover 800 square feet of road. If each truckload costs $75, and there's a 20% sales tax, how much will Mark need to pay for asphalt?"""
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