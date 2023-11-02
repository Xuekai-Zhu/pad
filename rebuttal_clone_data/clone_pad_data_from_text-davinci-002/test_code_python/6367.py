def solution():
    price_paid = 90
    selling_price = price_paid + 10
    tax = selling_price * 10 / 100
    profit = selling_price - tax - price_paid
    result = profit
    return result

print(solution())