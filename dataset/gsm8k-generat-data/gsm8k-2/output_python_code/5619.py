def solution():
    """To make room for a new inventory of books, Gordon's local bookstore is offering 30% off any book that is over $22.00 and 20% off any book under $20.00. He buys several books with the following prices; $25.00, $18.00, $21.00, $35.00, $12.00 and $10.00. How much will he spend on books?"""
    books = [25, 18, 21, 35, 12, 10]
    total_price = 0
    for price in books:
        if price > 22:
            total_price += price * 0.7
        elif price < 20:
            total_price += price * 0.8
        else:
            total_price += price

    result = total_price
    return result

print(solution())