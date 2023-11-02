def solution():
    """On Monday a group of 7 children and 5 adults went to the zoo. On Tuesday a group of 4 children and 2 adults went as well. Child tickets cost $3, and adult tickets cost $4. How much money did the zoo make in total for both days?"""
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