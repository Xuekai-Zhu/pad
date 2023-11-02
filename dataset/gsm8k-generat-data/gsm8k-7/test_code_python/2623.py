def solution():
    yellow_tickets = 8
    red_tickets = 3
    blue_tickets = 7

    # Calculate the total number of blue tickets needed to win a Bible
    total_blue_tickets_needed = 10 * 10 * 10 * 2

    # Calculate the total number of blue tickets Tom already has
    total_blue_tickets = blue_tickets + (red_tickets * 10) + (yellow_tickets * 10 * 10)

    # Calculate the number of additional blue tickets needed to win a Bible
    additional_blue_tickets_needed = total_blue_tickets_needed - total_blue_tickets
    result = additional_blue_tickets_needed
    return result

print(solution())