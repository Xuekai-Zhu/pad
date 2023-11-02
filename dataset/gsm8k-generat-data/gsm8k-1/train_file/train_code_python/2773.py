def solution():
    """Officer Hopps has to give out 200 tickets in May. The first 15 days he averages 8 tickets a day. How many does he have to average each day for the rest of the month to reach his required goal?"""
    goal_tickets = 200
    tickets_first_half = 15 * 8
    tickets_left = goal_tickets - tickets_first_half
    days_left = 31 - 15
    tickets_per_day = tickets_left / days_left
    result = tickets_per_day
    return result

print(solution())