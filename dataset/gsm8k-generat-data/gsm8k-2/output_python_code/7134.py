def solution():
    """Jan buys 5 dozen roses. Each rose cost $6. Since he bought so many he only needs to pay 80%. How much did he pay?"""
    dozen = 12
    total_roses = 5 * dozen
    price_per_rose = 6
    discount = 0.8
    total_price = total_roses * price_per_rose * discount
    result = total_price
    return result

print(solution())