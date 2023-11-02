def solution():
    # Pre-bought tickets
    num_prebought = 20
    price_prebought = 155
    total_prebought = num_prebought * price_prebought

    # Gate tickets
    num_gate = 30
    price_gate = 200
    total_gate = num_gate * price_gate

    # Difference in price paid
    difference = total_gate - total_prebought
    result = difference
    return result

print(solution())