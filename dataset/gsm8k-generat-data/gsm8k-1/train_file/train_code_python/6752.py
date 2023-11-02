def solution():
    """Amanda has to sell 80 tickets in 3 days so she can make enough money to go on vacation. On the first day, she sells 5 of her friends 4 tickets each. On the second day she sells 32 tickets. How many tickets does she need to sell on the third day to meet her goal?"""
    total_tickets_goal = 80
    tickets_sold_first_day = 5 * 4
    tickets_sold_second_day = 32
    tickets_remaining = total_tickets_goal - tickets_sold_first_day - tickets_sold_second_day
    tickets_needed_third_day = tickets_remaining / 1 #assuming she needs to sell all remaining tickets on the third day
    result = tickets_needed_third_day
    return result

print(solution())