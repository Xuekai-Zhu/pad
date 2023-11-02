def solution():
    """Officer Hopps has to give out 200 tickets in May. The first 15 days he averages 8 tickets a day. How many does he have to average each day for the rest of the month to reach his required goal?"""
    # Define the total required tickets and the number of days in May
    total_tickets = 200
    days_in_month = 31

    # Calculate the number of tickets given out in the first 15 days
    tickets_first_half = 15 * 8

    # Calculate the number of tickets still required
    tickets_remaining = total_tickets - tickets_first_half

    # Calculate the number of days remaining in the month
    days_remaining = days_in_month - 15

    # Calculate the number of tickets Officer Hopps needs to give out each day for the rest of the month
    ticket_per_day = tickets_remaining / days_remaining

    # Round up to the nearest whole number
    ticket_per_day = math.ceil(ticket_per_day)

    result = ticket_per_day
    return result

print(solution())