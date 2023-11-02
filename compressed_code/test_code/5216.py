def solution():
    
    total_tickets = 80
    sold_on_day1 = 5 * 4  
    sold_on_day2 = 32
    remaining_tickets = total_tickets - sold_on_day1 - sold_on_day2
    tickets_needed_on_day3 = remaining_tickets / 1  
    result = tickets_needed_on_day3
    return result

print(solution())