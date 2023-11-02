def solution():
    lobster_price = 25.50
    steak_price = 35.00
    burger_and_fries_price = 13.50
    appetizer_price = 8.50
    dessert_price = 6.00

    num_people = 4
    lobster_total = lobster_price * 1
    steak_total = steak_price * 1
    burger_and_fries_total = burger_and_fries_price * 2
    appetizer_total = appetizer_price * 1
    dessert_total = dessert_price * num_people

    sub_total = lobster_total + steak_total + burger_and_fries_total + appetizer_total + dessert_total
    tip = sub_total * 0.20
    total_bill = sub_total + tip

    result = total_bill
    return result

print(solution())