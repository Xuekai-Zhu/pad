def solution():
    ticket_cost = 20
    brothers_ticket_cost = 10
    money_saved = 5
    total_cost = ticket_cost + (brothers_ticket_cost * 2)
    weeks_needed = total_cost / 3
    result = weeks_needed
    return result

print(solution())