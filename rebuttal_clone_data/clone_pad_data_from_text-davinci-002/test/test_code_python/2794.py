def solution():
    sale_price = 500000
    markup = 20
    sale_price_with_markup = sale_price * (1 + (markup / 100))
    percent_tax = 10
    taxes = sale_price_with_markup * (percent_tax / 100)
    post_tax_sale_price = sale_price_with_markup - taxes
    split = post_tax_sale_price / 4
    result = split
    return result

print(solution())