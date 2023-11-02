def solution():
    total_money = 5000
    motorcycle_cost = 2800
    remaining_money = total_money - motorcycle_cost
    concert_ticket_cost = remaining_money / 2
    remaining_money -= concert_ticket_cost
    money_lost = remaining_money / 4
    remaining_money -= money_lost
    result = remaining_money
    return result

print(solution())