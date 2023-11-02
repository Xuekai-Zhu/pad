def solution():
    # Define the number of zebras
    zebras = 12

    # Calculate the number of camels
    camels = zebras / 2

    # Calculate the number of monkeys
    monkeys = camels * 4

    # Calculate the difference between the number of monkeys and giraffes
    giraffes = 2
    difference = monkeys - giraffes

    result = difference
    return result

print(solution())