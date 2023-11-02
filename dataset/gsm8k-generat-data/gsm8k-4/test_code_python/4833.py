def solution():
    """John wants to start a zoo. He has 15 snakes. He has twice as many monkeys as he does snakes. He has 5 fewer lions than he does monkeys. John has 8 more pandas than he does lions. John has 1/3 as many dogs as he does pandas. How many total animals does John have?"""
    # Define the number of snakes
    snakes = 15

    # Define the number of monkeys
    monkeys = snakes * 2

    # Define the number of lions
    lions = monkeys - 5

    # Define the number of pandas
    pandas = lions + 8

    # Define the number of dogs
    dogs = pandas / 3

    # Calculate the total number of animals
    total_animals = snakes + monkeys + lions + pandas + dogs

    # return the result
    result = total_animals
    return result

print(solution())