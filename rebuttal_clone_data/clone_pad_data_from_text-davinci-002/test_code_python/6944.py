def solution():
    cost_per_ticket = 2
    tickets_sold = 25
    total_cost = cost_per_ticket * tickets_sold
    donations = [15, 15, 20]
    total_donations = sum(donations)
    total_raised = total_cost + total_donations
    result = total_raised
    return result

print(solution())