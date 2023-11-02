def solution():
    # Define the given values
    total_tickets = 200
    first_half_days = 15
    first_half_tickets = 8 * first_half_days

    # Calculate how many tickets Officer Hopps has left to give out
    tickets_left = total_tickets - first_half_tickets

    # Calculate how many days Officer Hopps has left to give out the remaining tickets
    second_half_days = 31 - first_half_days

    # Calculate how many tickets Officer Hopps has to average per day in the second half of the month
    tickets_per_day = tickets_left / second_half_days
    result = tickets_per_day
    return result

print(solution())