def solution():
    """Brittany, Alex, and Jamy all share 600 marbles divided between them in the ratio 3:5:7. If Brittany gives Alex half of her marbles, what's the total number of marbles that Alex has?"""
    # Define the marbles ratios
    brittany_ratio = 3
    alex_ratio = 5
    jamy_ratio = 7

    # Calculate the total ratio
    total_ratio = brittany_ratio + alex_ratio + jamy_ratio

    # Calculate the number of marbles for each person according to the ratio
    brittany_marbles = (brittany_ratio / total_ratio) * 600
    alex_marbles = (alex_ratio / total_ratio) * 600
    jamy_marbles = (jamy_ratio / total_ratio) * 600

    # Brittany gives Alex half of her marbles
    brittany_marbles = brittany_marbles / 2
    alex_marbles = alex_marbles + brittany_marbles

    result = alex_marbles
    return result

print(solution())