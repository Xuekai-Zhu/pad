def solution():
    chickens_legs = 2  # Each chicken has 2 legs
    sheep_legs = 4  # Each sheep has 4 legs
    num_chickens = 7
    num_sheep = 5

    # Calculate the total number of legs of chickens and sheep
    total_legs = (chickens_legs * num_chickens) + (sheep_legs * num_sheep)
    result = total_legs
    return result

print(solution())