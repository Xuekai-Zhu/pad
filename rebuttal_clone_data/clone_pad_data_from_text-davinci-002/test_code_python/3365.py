def solution():
    shirt_price = 20
    shirt_quantity = 3
    tax_rate = 10
    total_price = shirt_price * shirt_quantity
    total_tax = total_price * (tax_rate / 100)
    result = total_price + total_tax
    return result

print(solution())