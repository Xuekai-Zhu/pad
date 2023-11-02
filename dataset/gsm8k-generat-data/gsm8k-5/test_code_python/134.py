def solution():
    adult_ticket = 109
    child_ticket = 109 - 5  # $5 discount for children below 12 years old
    total_cost = (2 * child_ticket) + (2 * adult_ticket)  # The couple has two children and two adults
    cash_given = 500
    change = cash_given - total_cost
    result = change
    return result

print(solution())