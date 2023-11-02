def solution():
    # Calculate total tickets sold on first two days
    total_tickets_sold = 5 * 4 + 32

    # Calculate remaining tickets to be sold to meet goal
    remaining_tickets = 80 - total_tickets_sold

    # Calculate tickets needed to sell on third day
    tickets_needed_on_third_day = remaining_tickets / 1    # Assuming she needs to sell all remaining tickets on third day

    result = tickets_needed_on_third_day
    return result

print(solution())