def solution():
    # define the cost of two cassette tapes and a headphone set
    cassette_tape_cost = 9*2
    headphone_set_cost = 25

    # calculate the total cost of the purchase
    total_cost = cassette_tape_cost + headphone_set_cost

    # calculate the amount of money Amanda will have left
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())