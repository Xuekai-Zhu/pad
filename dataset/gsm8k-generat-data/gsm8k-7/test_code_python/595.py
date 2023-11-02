def solution():
    total_bananas = 200
    lydia_bananas = 60
    dawn_bananas = lydia_bananas + 40
    donna_bananas = total_bananas - (lydia_bananas + dawn_bananas)
    result = donna_bananas
    return result

print(solution())