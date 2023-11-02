def solution():
    
    suits = 10
    dress_pants = 10
    dress_shirts_per_suit = 3
    suit_cost = 750
    dress_pants_cost = dress_pants_cost / 5
    dress_shirt_cost = 60
    total_cost = (suit_cost * suits) + (dress_pants_cost * dress_shirts_per_suit) + (dress_pants_cost * dress_shirts_cost)
    result = total_cost
    return result

print(solution())