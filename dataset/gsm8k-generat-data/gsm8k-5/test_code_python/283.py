def solution():
    num_tickets = 5
    ticket_cost = 1
    profit = 4
    total_revenue = (num_tickets / 2) * (2 * ticket_cost + (num_tickets - 1) * 1) + profit
    prize_money = total_revenue - profit
    result = prize_money
    return result

print(solution())