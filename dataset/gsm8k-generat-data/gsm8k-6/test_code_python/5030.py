def solution():
    # Calculate the total number of tickets sold in 6 minutes
    tickets_sold = 5 * 6  # metro sells an average of 5 tickets every minute for 6 minutes

    # Calculate the total earnings from the tickets sold
    total_earnings = tickets_sold * 3  # each ticket costs $3

    result = total_earnings
    return result

print(solution())