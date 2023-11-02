def solution():
    total_marbles = 600
    ratio = [3, 5, 7]
    total_ratio = sum(ratio)
    brittany_share = (ratio[0] / total_ratio) * total_marbles
    alex_share = (ratio[1] / total_ratio) * total_marbles
    jamy_share = (ratio[2] / total_ratio) * total_marbles

    # Brittany gives Alex half of her marbles
    brittany_gives = brittany_share / 2
    alex_share += brittany_gives

    result = alex_share
    return result

print(solution())