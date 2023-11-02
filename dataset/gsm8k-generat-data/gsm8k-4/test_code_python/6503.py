def solution():
    """Carla went to the zoo and counted 12 zebras in their enclosure. She then visited the camels and learned that there were only half as many camels as there were zebras. Next, she visited the monkeys and counted 4 times the number of monkeys as camels. Finally, she saw some giraffes and counted only 2 giraffes. How many more monkeys than giraffes did Carla see?"""
    # Define the number of zebras
    zebras = 12

    # Calculate the number of camels
    camels = zebras / 2

    # Calculate the number of monkeys
    monkeys = camels * 4

    # Calculate the number of giraffes
    giraffes = 2

    # Calculate the difference between the number of monkeys and giraffes
    difference = monkeys - giraffes

    # return the result
    result = difference
    return result

print(solution())