def solution():
    total_tickets = 80
    tickets_sold_day1 = 5 * 4
    tickets_sold_day2 = 32
    tickets_sold_day3 = total_tickets - tickets_sold_day1 - tickets_sold_day2
    result = tickets_sold_day3
    return result

print(solution())