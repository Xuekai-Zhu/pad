def solution():
    money_received = 50  # amount of money Amanda received
    tapes_cost = 2 * 9  # cost of two cassette tapes
    headphone_cost = 25  # cost of the headphone set
    total_cost = tapes_cost + headphone_cost  # total cost of the items
    money_left = money_received - total_cost  # money left after buying the items
    result = money_left
    return result

print(solution())