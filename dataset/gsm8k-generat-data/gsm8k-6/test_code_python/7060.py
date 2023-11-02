def solution():
    # Calculate the profit from selling the stocks and add it to Josh's wallet
    profit = 0.3 * 2000  # 30% increase in stock price
    total_money = 300 + 2000 + profit
    result = total_money - 2000  # subtract the initial investment
    return result

print(solution())