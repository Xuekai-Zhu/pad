def solution():
    # Calculate the amount James received from selling his old car
    sale_price = 0.8 * 20000  # 80% of the value of his old car

    # Calculate the amount James paid for the new car
    purchase_price = 0.9 * 30000  # 90% of the sticker price of the new car

    # Calculate the total amount James was out of pocket
    out_of_pocket = purchase_price - sale_price

    result = out_of_pocket
    return result

print(solution())