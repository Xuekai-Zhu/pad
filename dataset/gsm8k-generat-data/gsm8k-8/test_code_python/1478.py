def solution():
    total_cost = 750
    sneaker_cost = 200
    outfit_cost = 250
    racket_cost = total_cost - (sneaker_cost + outfit_cost)
    result = racket_cost
    return result

print(solution())