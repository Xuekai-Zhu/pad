def solution():
    """Diego baked 12 cakes for his sister's birthday. Donald also baked 4 cakes, but ate 1 while waiting for the party to start. How many cakes are left?"""
    diego_cakes = 12
    donald_cakes = 4
    cakes_eaten = 1
    total_cakes = diego_cakes + donald_cakes - cakes_eaten
    result = total_cakes
    return result

print(solution())