def solution():
    lucy_money = 20  # Lucy originally had $20
    lucy_gives = 5  # If Lucy gives Linda $5, they will have the same amount of money
    linda_money = lucy_money - lucy_gives  # Calculate how much money Linda had after Lucy gave her $5
    result = linda_money
    return result

print(solution())