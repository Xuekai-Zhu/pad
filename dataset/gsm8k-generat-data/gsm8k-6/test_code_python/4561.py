def solution():
    # Calculate the amount of money each person has
    jack_money = 26  # Jack has $26
    ben_money = jack_money + 9  # Ben has $9 more than Jack
    eric_money = ben_money - 10  # Eric has $10 less than Ben
    total_money = jack_money + ben_money + eric_money  # Calculate the total amount of money they have
    
    result = total_money
    return result

print(solution())