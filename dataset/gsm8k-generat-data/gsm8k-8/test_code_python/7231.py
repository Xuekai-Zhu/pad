def solution():
    money = 100
    scissor_cost = 5
    eraser_cost = 4
    num_scissors = 8
    num_erasers = 10

    total_scissors_cost = num_scissors * scissor_cost
    total_erasers_cost = num_erasers * eraser_cost
    total_cost = total_scissors_cost + total_erasers_cost
    money_remaining = money - total_cost
    result = money_remaining
    return result

print(solution())