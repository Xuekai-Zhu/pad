def solution():
    purchase_price = 250

    # Calculate the amount of discount received
    discount = (purchase_price // 100) * 10

    # Calculate the final price paid after the discount
    final_price = purchase_price - discount
    result = final_price
    return result

print(solution())