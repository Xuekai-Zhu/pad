def solution():
    bitcoin = 80
    charity = 20
    brother = bitcoin / 2
    bitcoin = bitcoin + (bitcoin * 3)
    charity = charity + 10
    result = bitcoin - charity - brother
    return result

print(solution())