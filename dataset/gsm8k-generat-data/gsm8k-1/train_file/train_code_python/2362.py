def solution():
    """There are twice as many centipedes as humans on a certain island and half as many sheep as humans. How many sheep and humans in total are on the island if the number of centipedes is 100?"""
    centipedes = 100
    humans = centipedes / 2
    sheep = humans / 2
    total = centipedes + humans + sheep
    result = total
    return result

print(solution())