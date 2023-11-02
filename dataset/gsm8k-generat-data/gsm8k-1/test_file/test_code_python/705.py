def solution():
    """An ice cream factory makes 100 quarts of chocolate ice cream in 2 hours. It can make 50 quarts of vanilla ice cream in 4 hours. How many quarts in total would be made in 48 hours?"""
    chocolate_rate = 50 # quarts per hour
    vanilla_rate = 12.5 # quarts per hour
    total_quarts = (chocolate_rate + vanilla_rate) * 48
    result = total_quarts
    return result

print(solution())