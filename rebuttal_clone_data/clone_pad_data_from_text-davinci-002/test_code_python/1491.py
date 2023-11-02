def solution():
    marbles_remaining = 400
    customer_count = 20
    marbles_bought = 15
    marbles_sold = customer_count * marbles_bought
    marbles_left = marbles_remaining - marbles_sold
    result = marbles_left
    return result

print(solution())