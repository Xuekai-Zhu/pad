def solution():
    """Antonella has ten Canadian coins in her purse that are either loonies or toonies. A loonie equals $1 and a toonie equals $2. If she bought a $3 Frappuccino and still has $11, how many toonies did she initially have?"""
    # Define the initial number of toonies
    toonies = None

    # Define the total amount of money in Antonella's purse
    total_money = 11 + 3  # $11 plus the cost of the Frappuccino

    # Try all possible combinations of toonies and loonies
    for i in range(11):  # i represents the number of toonies
        j = 10 - i  # j represents the number of loonies
        # Check if this combination of coins equals the total money in Antonella's purse
        if i * 2 + j == total_money:
            toonies = i
            break
    
    result = toonies
    return result

print(solution())