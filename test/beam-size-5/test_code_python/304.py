def solution():
    ice_cream_price = 13
    milk_price = 0.5
    num_ice_cream_tubs = 2
    num_milk_packets = 4

    # Calculate the total revenue from ice cream sales
    ice_cream_revenue = num_ice_cream_tubs * ice_cream_price

    # Calculate the total revenue from milk sales
    milk_revenue = num_milk_packets * milk_price

    # Calculate the total savings
    total_savings = ice_cream_revenue - milk_revenue
    result = total_savings
    return result

print(solution())