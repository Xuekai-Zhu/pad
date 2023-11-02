def solution():
    
    monday_children = 7
    monday_adults = 5
    tuesday_children = 4
    tuesday_adults = 2
    child_ticket_price = 3
    adult_ticket_price = 4
    monday_total = (monday_children * child_ticket_price) + (monday_adults * adult_ticket_price)
    tuesday_total = (tuesday_children * child_ticket_price) + (tuesday_adults * adult_ticket_price)
    total_earnings = monday_total + tuesday_total
    result = total_earnings
    return result

print(solution())