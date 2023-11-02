def solution():
    total_tickets = 200  # Officer Hopps has to give out 200 tickets in May
    tickets_given_first_half = 15 * 8  # Officer Hopps gave out 8 tickets per day for the first 15 days
    tickets_left_to_give = total_tickets - tickets_given_first_half  # Officer Hopps has tickets left to give
    days_left_to_give_tickets = 31 - 15  # There are 31 days in May and Officer Hopps has already worked for 15 days

    # Calculate the average number of tickets Officer Hopps must give out per day for the remaining days
    average_tickets_per_day = tickets_left_to_give / days_left_to_give_tickets
    result = average_tickets_per_day
    return result

print(solution())