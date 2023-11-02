def solution():
    
    ice_cream_cost = 3.5
    movie_tickets_cost = 7.5
    bracelet_cost = 8.5
    total_spent = ice_cream_cost + (2 * movie_tickets_cost) + bracelet_cost
    money_left = 40 - total_spent
    result = money_left
    return result

print(solution())