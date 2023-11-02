def solution():
    """Lyle wants to buy himself and his friends a sandwich and a pack of juice. 
    A sandwich costs $0.30 while a pack of juice costs $0.2. If Lyle has $2.50, 
    how many of his friends can have a sandwich and a pack of juice?"""
    
    lyle_money = 2.5
    sandwich_cost = 0.3
    juice_cost = 0.2
    
    total_cost = sandwich_cost + juice_cost
    friends_can_afford = int((lyle_money - total_cost) / total_cost)
    
    return friends_can_afford

print(solution())