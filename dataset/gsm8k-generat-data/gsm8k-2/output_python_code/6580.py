def solution():
    """Andy bakes and sells birthday cakes. To make two cakes he spends $12 on ingredients, and $1 on packaging for each cake. Andy sells each cake for $15. How much money does Andy make for each cake?"""
    total_cost = 12 + 2*1 # cost of ingredients for 2 cakes plus $1 packaging for each cake
    revenue = 2 * 15  # selling price of 2 cakes
    profit = revenue - total_cost
    profit_per_cake = profit / 2
    result = profit_per_cake
    return result

print(solution())