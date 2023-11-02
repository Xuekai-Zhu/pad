def solution():
    retail_price = 1000
    gc_discount = 0.15  # 15% discount
    gc_shipping_fee = 100
    sw_discount = 0.1  # 10% discount
    sw_shipping_fee = 0  # free shipping

    # Calculate the discounted price and total cost at Guitar Center
    gc_discounted_price = retail_price * (1 - gc_discount)
    gc_total_cost = gc_discounted_price + gc_shipping_fee

    # Calculate the discounted price and total cost at Sweetwater
    sw_discounted_price = retail_price * (1 - sw_discount)
    sw_total_cost = sw_discounted_price + sw_shipping_fee

    # Calculate the savings by buying from Sweetwater instead of Guitar Center
    savings = gc_total_cost - sw_total_cost
    result = savings
    return result

print(solution())