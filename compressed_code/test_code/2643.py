def solution():
    
    ticket_cost = 8
    popcorn_cost = 5
    drink_cost = 6
    candy_cost = 3

    normal_cost = ticket_cost + popcorn_cost + drink_cost + candy_cost

    deal_cost = 20

    savings = normal_cost - deal_cost

    result = savings
    return result

print(solution())