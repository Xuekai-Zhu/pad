def solution():
    """Lily has 5 lottery tickets to sell. She sells the first ticket for $1. She then sells each successive ticket for a dollar more than the previous ticket. She plans to keep a $4 profit and give the remaining money as the prize. How much money will the winner of the lottery receive?"""
    num_tickets = 5
    first_ticket_price = 1
    total_ticket_price = 0
    for i in range(num_tickets):
        total_ticket_price += first_ticket_price + i

    prize = total_ticket_price - 4
    result = prize
    return result

print(solution())