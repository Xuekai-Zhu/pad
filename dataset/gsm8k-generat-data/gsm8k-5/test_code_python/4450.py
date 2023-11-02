def solution():
    # Cost of tickets bought on the concert website
    cost_website_tickets = 2 * 50

    # Cost of tickets bought from the scalper
    cost_scalper_tickets = 2 * 50 * 2.4 - 10

    # Cost of the discounted ticket
    cost_discounted_ticket = 50 * 0.6

    # Total cost of all tickets
    total_cost = cost_website_tickets + cost_scalper_tickets + cost_discounted_ticket

    # Cost per friend
    cost_per_friend = total_cost / 5

    result = cost_per_friend
    return result

print(solution())