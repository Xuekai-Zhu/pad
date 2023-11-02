def solution():
    # Define the number of centipedes on the island
    centipedes = 100

    # Define the ratio of centipedes to humans as 2:1
    centipedes_to_humans = 2/1

    # Calculate the number of humans on the island
    humans = centipedes / centipedes_to_humans

    # Calculate the number of sheep on the island as half the number of humans
    sheep = humans / 2

    # Calculate the total number of humans and sheep on the island
    total = humans + sheep
    result = total
    return result

print(solution())