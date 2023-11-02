def solution():
    # Calculate the total number of bracelets Robin needs to buy
    total_bracelets = len("Jessica") + len("Tori") + len("Lily") + len("Patrice")  

    # Calculate the total cost
    total_cost = total_bracelets * 2  # each bracelet costs $2
    result = total_cost
    return result

print(solution())