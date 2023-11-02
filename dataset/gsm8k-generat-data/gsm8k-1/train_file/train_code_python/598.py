def solution():
    """John pays for a candy bar with 4 quarters, 3 dimes, and a nickel. He got 4 cents back in change. How many cents did the candy bar cost?"""
    quarters = 4
    dimes = 3
    nickel = 1
    total_paid = (quarters * 25) + (dimes * 10) + (nickel * 5)
    change = 4
    candy_bar_cost = total_paid - change
    result = candy_bar_cost
    return result

print(solution())