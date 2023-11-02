def solution():
    num_centipedes = 100

    # Since there are twice as many centipedes as humans, the number of humans is half the number of centipedes
    num_humans = num_centipedes / 2

    # Since there are half as many sheep as humans, the number of sheep is half the number of humans
    num_sheep = num_humans / 2

    # Calculate the total number of humans and sheep on the island
    total = num_humans + num_sheep
    result = total
    return result

print(solution())