def solution():
    """John buys 20 candy bars. His brother Dave pays for 6 of them. If each candy bar costs $1.50, how much did John pay?"""
    candy_bar_price = 1.5
    john_buys = 20 - 6
    john_paid = john_buys * candy_bar_price
    result = john_paid
    return result

print(solution())