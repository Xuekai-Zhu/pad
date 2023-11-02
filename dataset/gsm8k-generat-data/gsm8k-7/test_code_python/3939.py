def solution():
    pauline_price = 30
    jean_price = pauline_price - 10
    ida_price = jean_price + 30
    patty_price = ida_price + 10

    # Calculate the total cost of all dresses
    total_cost = pauline_price + jean_price + ida_price + patty_price
    result = total_cost
    return result

print(solution())