def solution():
    snakes = 15
    monkeys = snakes * 2
    lions = monkeys - 5
    pandas = lions + 8
    dogs = pandas / 3
    total_animals = snakes + monkeys + lions + pandas + dogs
    result = total_animals
    return result

print(solution())