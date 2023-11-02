def solution():
    total_marbles = 100
    clear_marbles = 40
    black_marbles = 20
    other_marbles = total_marbles - clear_marbles - black_marbles
    friend_takes = 5
    friend_gets = friend_takes * (other_marbles / total_marbles)
    result = friend_gets
    
    return result

print(solution())