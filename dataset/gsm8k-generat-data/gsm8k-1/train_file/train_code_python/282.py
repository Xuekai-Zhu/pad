def solution():
    """Lily has 5 lottery tickets to sell. She sells the first ticket for $1. She then sells each successive ticket for a dollar more than the previous ticket. She plans to keep a $4 profit and give the remaining money as the prize. How much money will the winner of the lottery receive?"""
    num_tickets = 5
    base_price = 1
    total_price = 0
    for i in range(num_tickets):
        total_price += base_price + i
    
    total_price -= 4
    prize_money = total_price / 2
    result = prize_money
    return result

print(solution())