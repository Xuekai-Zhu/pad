def solution():
    starting_marbles = 400  # There are 400 marbles in the store at the start of the day
    customers = 20  # There are 20 customers who buy marbles
    marbles_bought = customers * 15  # Each customer buys 15 marbles
    marbles_remaining = starting_marbles - marbles_bought
    result = marbles_remaining
    return result

print(solution())