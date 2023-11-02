def solution():
    """It's strawberry-picking time on Grandma Concetta's farm. Tony can pick 6 quarts of strawberries per hour, while Bobby picks one less quart of strawberries per hour than Tony. Kathy can pick twice as many strawberries per hour as Bobby, and Ricky picks two fewer quarts of strawberries per hour than does Kathy. In total, how many quarts of strawberries can Tony, Bobby, Ricky, and Kathy pick per hour on Grandma Concetta's farm?"""
    tony = 6
    bobby = tony - 1
    kathy = bobby * 2
    ricky = kathy - 2
    total = tony + bobby + kathy + ricky
    result = total
    return result

print(solution())