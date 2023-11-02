def solution():
    """Amanda has to sell 80 tickets in 3 days so she can make enough money to go on vacation. On the first day, she sells 5 of her friends 4 tickets each. On the second day she sells 32 tickets. How many tickets does she need to sell on the third day to meet her goal?"""
    total_tickets = 80
    sold_on_day1 = 5 * 4  # Amanda sold 4 tickets each to 5 friends
    sold_on_day2 = 32
    remaining_tickets = total_tickets - sold_on_day1 - sold_on_day2
    tickets_needed_on_day3 = remaining_tickets / 1  # assuming Amanda needs to sell all remaining tickets on the third day
    result = tickets_needed_on_day3
    return result

print(solution())