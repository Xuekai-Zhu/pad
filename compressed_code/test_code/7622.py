def solution():
    
    num_people = 4
    lobster_price = 25.50
    steak_price = 35.00
    burger_price = 13.50
    appetizer_price = 8.50
    dessert_price = 6.00
    tip_percent = 20

    meal_subtotal = lobster_price + steak_price + (2 * burger_price) + appetizer_price + (4 * dessert_price)
    tip_amount = meal_subtotal * (tip_percent / 100)
    total_bill = meal_subtotal + tip_amount
    
    result = total_bill
    return result

print(solution())