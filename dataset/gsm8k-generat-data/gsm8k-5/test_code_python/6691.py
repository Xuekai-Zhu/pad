def solution():
    money_received = 50  # Amanda received $50 as a gift
    cost_of_cassettes = 2 * 9  # Amanda plans to buy 2 cassette tapes that cost $9 each
    cost_of_headphones = 25  # Amanda plans to buy a headphone set that costs $25

    # Calculate the total cost of the items Amanda plans to buy
    total_cost = cost_of_cassettes + cost_of_headphones

    # Calculate the amount of money Amanda will have left after buying the items
    money_left = money_received - total_cost
    result = money_left
    return result

print(solution())