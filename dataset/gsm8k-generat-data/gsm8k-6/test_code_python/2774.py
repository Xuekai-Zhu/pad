def solution():
    # Calculate the number of tickets given by Officer Hopps in the first 15 days
    tickets_first_half = 15 * 8

    # Calculate the number of tickets remaining to be given in the second half of May
    tickets_remaining = 200 - tickets_first_half

    # Calculate the average number of tickets Officer Hopps needs to give each day in the second half of May
    average_per_day = tickets_remaining / 16  # May has 31 days and the first 15 days are already done

    result = average_per_day
    return result

print(solution())