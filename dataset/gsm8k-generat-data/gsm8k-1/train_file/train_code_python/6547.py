def solution():
    """Noah and Ava are planning a trip to the zoo. Zoo entry tickets are $5 per person. Bus fare is $1.50 per person one way. If they bring $40 with them, how much money do they have left to spend on lunch and snacks?"""
    num_people = 2
    entry_ticket_cost = 5
    bus_fare_cost = 1.5 * 2 * 2 # round trip for 2 people
    total_cost = num_people * (entry_ticket_cost + bus_fare_cost)
    remaining_money = 40 - total_cost
    result = remaining_money
    return result

print(solution())