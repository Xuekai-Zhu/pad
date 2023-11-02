def solution():
    rice_kilograms = 5
    rice_price = 2
    meat_pounds = 3
    meat_price = 5
    total_rice_price = rice_kilograms * rice_price
    total_meat_price = meat_pounds * meat_price
    total_price = total_rice_price + total_meat_price
    result = total_price
    return result

print(solution())