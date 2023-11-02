def solution():
    """Brittany, Alex, and Jamy all share 600 marbles divided between them in the ratio 3:5:7. If Brittany gives Alex half of her marbles, what's the total number of marbles that Alex has?"""
    total_ratio = 3 + 5 + 7
    brittany_share = (3/total_ratio) * 600
    alex_share = (5/total_ratio) * 600
    jamy_share = (7/total_ratio) * 600
    brittany_share = brittany_share - (brittany_share / 2)
    total_marbles = brittany_share + alex_share + jamy_share
    result = alex_share
    return result

print(solution())