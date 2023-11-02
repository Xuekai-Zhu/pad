def solution():
    total_tickets = 30 * 100  # 30 rolls of tickets with 100 tickets each
    tickets_bought_by_4th_graders = total_tickets * 0.3
    tickets_remaining = total_tickets - tickets_bought_by_4th_graders
    tickets_bought_by_5th_graders = tickets_remaining * 0.5
    tickets_remaining = tickets_remaining - tickets_bought_by_5th_graders
    tickets_remaining = tickets_remaining - 100  # 6th graders bought 100 tickets
    result = tickets_remaining
    return result

print(solution())