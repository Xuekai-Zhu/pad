def solution():
    # Calculate the number of monkeys, lions, pandas, and dogs John has
    monkeys = 2 * 15  # John has twice as many monkeys as he does snakes
    lions = monkeys - 5  # John has 5 fewer lions than he does monkeys
    pandas = lions + 8  # John has 8 more pandas than he does lions
    dogs = int(pandas / 3)  # John has 1/3 as many dogs as he does pandas

    # Calculate the total number of animals John has
    total_animals = 15 + monkeys + lions + pandas + dogs
    result = total_animals
    return result

print(solution())