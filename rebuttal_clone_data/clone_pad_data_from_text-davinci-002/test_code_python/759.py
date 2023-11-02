def solution():
    total_flour = 500
    bags_of_flour = total_flour / 50
    cost_of_flour = bags_of_flour * 20
    total_salt = 10
    cost_of_salt = total_salt * .2
    advertising = 1000
    ticket_sales = 500 * 20
    total_cost = cost_of_flour + cost_of_salt + advertising
    profit = ticket_sales - total_cost
    result = profit
    return result

print(solution())