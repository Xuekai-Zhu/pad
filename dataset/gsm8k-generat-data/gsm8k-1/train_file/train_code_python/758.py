def solution():
    """Tom wants to make the world's largest dough ball. He needs 500 pounds of flour and he can buy 50-pound bags of flour for $20. He also needs 10 pounds of salt and salt cost $.2 a pound. He also spends $1000 promoting everything. He then sells tickets for $20 each and sells 500 tickets. How much money did he make?"""
    flour_cost = (500 // 50) * 20
    salt_cost = 10 * 0.2
    total_cost = flour_cost + salt_cost + 1000
    revenue = 20 * 500
    profit = revenue - total_cost
    result = profit
    return result

print(solution())