def solution():
    """Whitney’s mom gave her two $20 bills to spend at the school book fair. Whitney has decided to buy 2 posters, 3 notebooks, and 2 bookmarks. Each poster costs $5, each notebook costs $4, and each bookmark costs $2. How much money, in dollars, will Whitney have left over after the purchase?"""
    total_cost = (2 * 5) + (3 * 4) + (2 * 2)
    total_payment = 2 * 20
    leftover = total_payment - total_cost
    result = leftover
    return result

print(solution())