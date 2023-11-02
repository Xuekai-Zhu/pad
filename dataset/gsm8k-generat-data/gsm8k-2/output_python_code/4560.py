def solution():
    """Eric, Ben, and Jack have some money. Eric has $10 less than Ben, and Ben has $9 less than Jack. If Jack has $26, how much money, in dollars, do all 3 of them have in total?"""
    jack_money = 26
    ben_money = jack_money + 9
    eric_money = ben_money - 10
    total_money = jack_money + ben_money + eric_money
    result = total_money
    return result

print(solution())