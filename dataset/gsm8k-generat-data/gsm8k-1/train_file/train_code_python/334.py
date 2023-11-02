def solution():
    """Eve wants to buy her 3 nieces cooking gear that's made for kids. The hand mitts cost $14.00 and the apron is $16.00. A set of 3 cooking utensils is $10.00 and a small knife is twice the amount of the utensils. The store is offering a 25% off sale on all cooking gear. How much will Eve spend on the gifts?"""
    mitts_price = 14
    apron_price = 16
    utensils_price = 10
    knife_price = utensils_price * 2
    total_price_before_sale = (mitts_price + apron_price + (utensils_price * 3) + knife_price)
    total_price_after_sale = total_price_before_sale - (total_price_before_sale * 0.25)
    final_price_for_3_nieces = total_price_after_sale * 3
    result = final_price_for_3_nieces
    return result

print(solution())