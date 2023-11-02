def solution():
    burgers_sold = 30
    fries_sold = 12
    burger_price = 2
    fries_price = 1.5
    burger_earnings = burgers_sold * burger_price
    fries_earnings = fries_sold * fries_price
    spongbob_earnings = burger_earnings + fries_earnings
    result = spongbob_earnings
    return result

print(solution())