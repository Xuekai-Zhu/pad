def solution():
    adult_ticket_price = 26
    child_ticket_price = adult_ticket_price / 2
    total_attendees = 183 + 28
    total_revenue = (adult_ticket_price * 183) + (child_ticket_price * 28)
    result = total_revenue
    return result

print(solution())