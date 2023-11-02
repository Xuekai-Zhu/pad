def solution():
    # Calculate the total number of donuts Chris buys
    total_donuts = 2.5 * 12  # 1 dozen is 12 donuts

    # Calculate the number of donuts Chris eats while driving
    donuts_eaten = 0.1 * total_donuts

    # Calculate the number of donuts Chris has left after eating and snacking
    donuts_left = total_donuts - donuts_eaten - 4

    result = donuts_left
    return result

print(solution())