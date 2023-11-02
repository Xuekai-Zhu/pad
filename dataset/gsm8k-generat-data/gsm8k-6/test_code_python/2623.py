def solution():
    # Calculate the total number of blue tickets Tom Sawyer has obtained
    blue_tickets = 7 + 3 * 10 + 8 * 10 * 10  # 7 blue tickets earned directly plus 3 red tickets exchanged plus 8 yellow tickets exchanged
    blue_tickets_needed = 10 * 10 * 10  # to win a new Bible, Tom Sawyer needs 10 yellow tickets, which are 10 red tickets each, which are 10 blue tickets each
    
    # Calculate the number of additional blue tickets needed to win a new Bible
    additional_blue_tickets_needed = blue_tickets_needed - blue_tickets
    result = additional_blue_tickets_needed
    return result

print(solution())