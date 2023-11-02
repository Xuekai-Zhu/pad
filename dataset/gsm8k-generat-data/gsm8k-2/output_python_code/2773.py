def solution():
    """Officer Hopps has to give out 200 tickets in May. The first 15 days he averages 8 tickets a day. How many does he have to average each day for the rest of the month to reach his required goal?"""
    total_tickets = 200
    tickets_first_half = 8 * 15
    tickets_second_half = total_tickets - tickets_first_half
    days_second_half = 31 - 15
    average_daily_tickets = tickets_second_half / days_second_half
    result = average_daily_tickets
    return result

print(solution())