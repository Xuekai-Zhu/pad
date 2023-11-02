def solution():
    """John wants to start a zoo. He has 15 snakes. He has twice as many monkeys as he does snakes. He has 5 fewer lions than he does monkeys. John has 8 more pandas than he does lions. John has 1/3 as many dogs as he does pandas. How many total animals does John have?"""
    snakes = 15
    monkeys = snakes * 2
    lions = monkeys - 5
    pandas = lions + 8
    dogs = pandas / 3
    total_animals = snakes + monkeys + lions + pandas + dogs
    result = total_animals
    return result

print(solution())