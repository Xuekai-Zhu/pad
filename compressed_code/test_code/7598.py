def solution():
    
    total_marbles = 600
    ratio_brittany = 3
    ratio_alex = 5
    ratio_jamy = 7
    total_ratio = ratio_brittany + ratio_alex + ratio_jamy
    marbles_alex = (ratio_alex / total_ratio) * total_marbles
    marbles_brittany = (ratio_brittany / total_ratio) * total_marbles
    new_marbles_brittany = marbles_brittany / 2
    marbles_alex += new_marbles_brittany
    result = marbles_alex
    return result

print(solution())