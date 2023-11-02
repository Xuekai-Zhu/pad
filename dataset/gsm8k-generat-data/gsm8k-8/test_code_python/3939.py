def solution():
    # Define the prices of the dresses
    pauline_price = 30
    jean_price = pauline_price - 10
    ida_price = jean_price + 30
    patty_price = ida_price + 10

    # Calculate the total spent on dresses
    total_spent = pauline_price + jean_price + ida_price + patty_price
    result = total_spent
    return result

print(solution())