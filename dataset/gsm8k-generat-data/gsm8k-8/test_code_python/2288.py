def solution():
    # Calculate the total ratio
    total_ratio = 3 + 5 + 7

    # Calculate the number of marbles for each person
    brittany_marbles = (3/total_ratio) * 600
    alex_marbles = (5/total_ratio) * 600
    jamy_marbles = (7/total_ratio) * 600

    # Brittany gives Alex half of her marbles
    brittany_marbles = brittany_marbles / 2
    alex_marbles = alex_marbles + brittany_marbles

    result = alex_marbles
    return result

print(solution())