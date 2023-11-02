def solution():
    num_eggplants = 20
    eggplant_price = 3
    num_corn = 25
    total_price = 135

    # Calculate the total revenue from selling all eggplants
    total_eggplant_revenue = num_eggplants * eggplant_price

    # Calculate the total revenue from selling all corn
    total_corn_revenue = total_price - total_eggplant_revenue

    # Calculate the price per ear of corn
    price_per_ear = total_corn_revenue / num_corn
    result = price_per_ear
    return result

print(solution())