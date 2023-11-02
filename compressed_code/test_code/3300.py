def solution():
    
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles * 1.25
    both_marbles = wolfgang_marbles + ludo_marbles
    michael_marbles = both_marbles * (2/3)
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    each_gets = total_marbles / 3
    result = each_gets
    return result

print(solution())