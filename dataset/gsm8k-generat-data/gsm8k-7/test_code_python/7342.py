def solution():
    shirt_price = 10
    num_shirts = 3

    if num_shirts == 1:
        total_cost = shirt_price
    elif num_shirts == 2:
        total_cost = shirt_price + (shirt_price * 0.5)
    elif num_shirts == 3:
        total_cost = shirt_price + (shirt_price * 0.5) + (shirt_price * 0.4)

    original_cost = (num_shirts * shirt_price)
    money_saved = original_cost - total_cost
    result = money_saved
    return result

print(solution())