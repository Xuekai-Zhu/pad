def solution():
    cost = 50  # cost of the book
    marked_price = cost * 1.3  # price after being marked up by 30%
    sale_price = marked_price * 0.9  # price after a 10% discount is given
    profit = sale_price - cost  # profit from selling the book
    percent_profit = (profit / cost) * 100  # calculate the percent profit
    result = percent_profit
    return result

print(solution())