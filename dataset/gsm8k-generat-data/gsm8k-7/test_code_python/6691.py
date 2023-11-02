def solution():
    gift_money = 50
    cost_cassette_tape = 9
    num_cassette_tape = 2
    cost_headphone = 25

    # Calculate the total cost of the two cassette tapes
    total_cassette_tape_cost = cost_cassette_tape * num_cassette_tape

    # Calculate the total cost of all items purchased
    total_cost = total_cassette_tape_cost + cost_headphone

    # Calculate the amount of money left after buying all items
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())