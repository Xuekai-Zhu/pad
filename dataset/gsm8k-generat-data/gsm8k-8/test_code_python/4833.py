def solution():
    # Define the number of snakes John has
    snakes = 15

    # Calculate the number of monkeys John has, which is twice the number of snakes
    monkeys = 2 * snakes

    # Calculate the number of lions John has, which is 5 fewer than the number of monkeys
    lions = monkeys - 5

    # Calculate the number of pandas John has, which is 8 more than the number of lions
    pandas = lions + 8

    # Calculate the number of dogs John has, which is 1/3 the number of pandas
    dogs = pandas / 3

    # Calculate the total number of animals John has
    total_animals = snakes + monkeys + lions + pandas + dogs

    result = total_animals
    return result

print(solution())