def solution():
    """Tom bought his games for $200. They tripled in value and he then sold 40% of them. How much did he sell the games for?"""
    initial_cost = 200
    value_after_tripling = initial_cost * 3
    amount_sold = 0.4 * value_after_tripling
    result = amount_sold
    return result

print(solution())