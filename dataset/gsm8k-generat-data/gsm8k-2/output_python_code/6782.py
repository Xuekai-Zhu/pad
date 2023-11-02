def solution():
    """Lyle wants to buy himself and his friends a sandwich and a pack of juice. A sandwich costs $0.30 while a pack of juice costs $0.2. If Lyle has $2.50, how many of his friends can have a sandwich and a pack of juice?"""
    lyle_budget = 2.5
    sandwich_price = 0.3
    juice_price = 0.2
    total_price = sandwich_price + juice_price
    friends_count = int((lyle_budget - total_price) / total_price)

    result = friends_count
    return result

print(solution())