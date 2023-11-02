def solution():
    num_dozen_donuts = 2.5
    num_donuts_per_dozen = 12
    total_donuts = num_dozen_donuts * num_donuts_per_dozen

    # Calculate the number of donuts Chris eats while driving
    eaten_while_driving = total_donuts * 0.1

    # Calculate the number of donuts Chris has left when he gets to work
    remaining_donuts = total_donuts - eaten_while_driving

    # Add the donuts Chris takes for his afternoon snack
    remaining_donuts += 4

    result = remaining_donuts
    return result

print(solution())