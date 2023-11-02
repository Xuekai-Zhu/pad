def solution():
    num_wins = []
    num_wins.append(40)
    num_wins.append((5/8)*num_wins[0])
    num_wins.append(num_wins[0]+num_wins[1])
    total_num_wins = sum(num_wins)
    result = total_num_wins
    
    return result

print(solution())