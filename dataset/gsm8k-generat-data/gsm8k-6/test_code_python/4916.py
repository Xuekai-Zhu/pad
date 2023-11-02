def solution():
    # Calculate the remaining number of fruits after Luisa has taken some from the bag
    apples_remaining = 7 - 2  # Luisa takes out 2 apples
    oranges_remaining = 8 - 2*2  # Luisa takes out twice as many oranges as apples
    mangoes_remaining = 15 - (2/3)*15  # Luisa takes out 2/3 of the mangoes
    total_remaining = apples_remaining + oranges_remaining + mangoes_remaining
    result = total_remaining
    return result

print(solution())