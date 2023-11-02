def solution():
    starting_money = 5000
    motorcycle_cost = 2800

    # Calculate the money remaining after buying the motorcycle
    money_remaining = starting_money - motorcycle_cost

    # Calculate the cost of the concert ticket
    concert_ticket_cost = money_remaining / 2

    # Calculate the money remaining after buying the concert ticket
    money_remaining = money_remaining - concert_ticket_cost

    # Calculate the amount Jake loses after losing a fourth of what he has left
    lost_money = money_remaining / 4

    # Calculate the money remaining after losing some money
    money_remaining = money_remaining - lost_money
    result = money_remaining
    return result

print(solution())