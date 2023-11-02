def solution():
    
    lobster_price = 25.50
    steak_price = 35.00
    cheeseburger_price = 13.50
    appetizer_price = 8.50
    dessert_price = 6.00
    number_of_people = 4

    total_price = lobster_price + steak_price + 2*cheeseburger_price + appetizer_price + 4*dessert_price
    tip = total_price * 0.20
    final_bill = total_price + tip
    result = final_bill
    return result

print(solution())