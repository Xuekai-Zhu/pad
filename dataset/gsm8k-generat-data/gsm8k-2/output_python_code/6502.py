def solution():
    """Carla went to the zoo and counted 12 zebras in their enclosure. She then visited the camels and learned that there were only half as many camels as there were zebras. Next, she visited the monkeys and counted 4 times the number of monkeys as camels. Finally, she saw some giraffes and counted only 2 giraffes. How many more monkeys than giraffes did Carla see?"""
    zebras = 12
    camels = zebras / 2
    monkeys = 4 * camels
    giraffes = 2
    monkey_giraffe_difference = monkeys - giraffes
    result = monkey_giraffe_difference
    return result

print(solution())