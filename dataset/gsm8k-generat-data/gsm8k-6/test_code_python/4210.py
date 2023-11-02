def solution():
    # Calculate the number of croissants needed for 2 sandwiches per person
    total_croissants = 2 * 24  

    # Calculate the number of croissant packs needed
    croissant_packs = total_croissants / 12

    # Calculate the cost of the croissants
    cost = croissant_packs * 8

    result = cost
    return result

print(solution())