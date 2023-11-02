def solution():
    num_cakes = 320 # number of cakes she made on the sixth day
    for day in range(6,0,-1):
        num_cakes = num_cakes/2  # on each previous day, she made half as many cakes
    result = num_cakes
    return result

print(solution())