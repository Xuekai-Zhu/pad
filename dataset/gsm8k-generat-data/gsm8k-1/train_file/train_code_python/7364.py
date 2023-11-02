def solution():
    """Frank and Bill have $42 and they bought 3 large pizzas with the money. Each pizza cost $11 and Frank paid for all three pizzas. Frank gave the rest of his money to Bill. If Bill had $30 already, how much money does Bill have now?"""
    total_cost = 11 * 3
    frank_paid = total_cost
    remaining_money = 42 - frank_paid
    bill_money = remaining_money + 30
    result = bill_money
    return result

print(solution())