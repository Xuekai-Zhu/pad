def solution():
    apples_per_bushel = 48  # Each bushel contains 48 apples
    cost_per_bushel = 12  # Bronson buys each bushel from farmers for $12
    price_per_apple = 0.40  # Bronson sells each apple to grocery stores for $0.40

    # Calculate the profit per apple
    profit_per_apple = price_per_apple - (cost_per_bushel/apples_per_bushel)

    # Calculate the total profit after selling 100 apples
    total_profit = 100 * profit_per_apple
    result = total_profit
    return result

print(solution())