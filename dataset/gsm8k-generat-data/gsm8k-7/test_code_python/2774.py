def solution():
    total_tickets = 200
    first_15_days_tickets = 15 * 8

    # Calculate the number of tickets needed for the rest of the month
    tickets_left = total_tickets - first_15_days_tickets
    days_left = 31 - 15
    average_tickets_needed = tickets_left / days_left

    result = average_tickets_needed
    return result

print(solution())