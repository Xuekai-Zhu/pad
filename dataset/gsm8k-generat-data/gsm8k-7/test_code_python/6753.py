def solution():
    total_tickets_goal = 80
    days_left = 3

    # Calculate the number of tickets Amanda has sold so far
    tickets_sold_so_far = (5 * 4) + 32

    # Calculate the number of tickets Amanda still needs to sell
    tickets_left_to_sell = total_tickets_goal - tickets_sold_so_far

    # Calculate the average number of tickets Amanda needs to sell per day to meet her goal
    average_tickets_per_day = tickets_left_to_sell / days_left

    result = average_tickets_per_day
    return result

print(solution())