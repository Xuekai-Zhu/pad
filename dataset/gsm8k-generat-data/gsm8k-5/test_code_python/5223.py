def solution():
    # Calculate the total earnings from selling burgers
    burgers_sold = 30
    burger_price = 2
    burger_earnings = burgers_sold * burger_price

    # Calculate the total earnings from selling large fries
    fries_sold = 12
    fries_price = 1.5
    fries_earnings = fries_sold * fries_price

    # Calculate the total earnings for the day
    total_earnings = burger_earnings + fries_earnings
    result = total_earnings
    return result

print(solution())