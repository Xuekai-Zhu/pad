def solution():
    # Calculate the total amount still owed
    total_still_owed = 400 - 285
    
    # Calculate how much Derek owes
    amy_owed = 30
    derek_owed = amy_owed / 2
    
    # Calculate how much Sally and Carl together owe
    sally_carl_owed = total_still_owed - amy_owed - derek_owed
    
    # Divide that amount by 2 to find how much each of them owed
    sally_carl_each_owed = sally_carl_owed / 2
    result = sally_carl_each_owed
    return result

print(solution())