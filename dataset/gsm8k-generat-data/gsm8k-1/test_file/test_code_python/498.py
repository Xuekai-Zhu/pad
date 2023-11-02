def solution():
    """Cherrie wants to buy Christmas gifts for her 5 friends. 2 of her friends want 5 gifts and the other 3 friends want 2 gifts for themselves. Cherrie goes ahead and buys them and decides to further surprise them by getting 10 more random gifts. How many gifts did Cherrie buy in total?"""
    total_friends = 5
    gifts_per_friend_1 = 5
    gifts_per_friend_2 = 5
    gifts_per_friend_3 = 2
    gifts_per_friend_4 = 2
    gifts_per_friend_5 = 2
    extra_gifts = 10
    
    total_gifts = (gifts_per_friend_1 + gifts_per_friend_2) + (gifts_per_friend_3 + gifts_per_friend_4 + gifts_per_friend_5) + extra_gifts
    result = total_gifts
    
    return result

print(solution())