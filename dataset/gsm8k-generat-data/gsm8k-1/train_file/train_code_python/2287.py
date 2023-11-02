def solution():
    """Brittany, Alex, and Jamy all share 600 marbles divided between them in the ratio 3:5:7. If Brittany gives Alex half of her marbles, what's the total number of marbles that Alex has?"""
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