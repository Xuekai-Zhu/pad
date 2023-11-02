def solution():
    """Noah and Ava are planning a trip to the zoo. Zoo entry tickets are $5 per person. Bus fare is $1.50 per person one way. If they bring $40 with them, how much money do they have left to spend on lunch and snacks?"""
    total_budget = 40
    num_people = 2
    ticket_price = 5
    bus_price = 1.5 * 2 * 2  # round trip for two people
    total_cost = ticket_price * num_people + bus_price
    remaining_budget = total_budget - total_cost
    result = remaining_budget
    return result

print(solution())