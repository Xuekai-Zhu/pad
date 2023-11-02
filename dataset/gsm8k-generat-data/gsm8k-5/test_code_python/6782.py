def solution():
    hendricks_price = 200  # Hendricks bought the guitar for $200
    discount_percent = 20  # Hendricks received a 20% discount
    discount_amount = hendricks_price * (discount_percent/100)  # Calculate the amount of the discount
    gerald_price = hendricks_price + discount_amount  # Calculate the original price that Gerald paid
    result = gerald_price
    return result

print(solution())