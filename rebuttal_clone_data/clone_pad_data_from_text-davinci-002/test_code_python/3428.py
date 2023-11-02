def solution():
    number_of_tickets = 24
    cost_per_ticket = 7
    discount_percentage = 50
    discount_amount = cost_per_ticket * (discount_percentage / 100)
    total_cost = number_of_tickets * cost_per_ticket - discount_amount
    result = total_cost
    return result

print(solution())