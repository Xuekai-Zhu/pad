def solution():
    total_bananas = 200  # Total number of bananas
    lydia_bananas = 60  # Lydia has 60 bananas
    dawn_bananas = lydia_bananas + 40  # Dawn has 40 more bananas than Lydia
    donna_bananas = total_bananas - (lydia_bananas + dawn_bananas)  # Donna has the remaining bananas

    result = donna_bananas
    return result

print(solution())