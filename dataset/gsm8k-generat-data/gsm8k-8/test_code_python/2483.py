def solution():
    gift_amount = 50
    cassette_cost = 9
    headphone_cost = 25

    total_cost = (2 * cassette_cost) + headphone_cost
    money_left = gift_amount - total_cost
    result = money_left
    return result

print(solution())