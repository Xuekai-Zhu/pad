def solution():
    # Given that there are twice as many centipedes as humans, divide the number of centipedes by 2 to get the number of humans
    centipedes = 100
    humans = centipedes / 2

    # Given that there are half as many sheep as humans, multiply the number of humans by 0.5 to get the number of sheep
    sheep = humans * 0.5

    # Calculate the total number of humans and sheep on the island
    total_population = humans + sheep

    result = total_population
    return result

print(solution())