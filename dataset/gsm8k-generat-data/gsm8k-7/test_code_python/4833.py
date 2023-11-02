def solution():
    num_snakes = 15
    num_monkeys = num_snakes * 2
    num_lions = num_monkeys - 5
    num_pandas = num_lions + 8
    num_dogs = int(num_pandas / 3)  # Assume all dogs are whole animals

    # Calculate the total number of animals
    total_animals = num_snakes + num_monkeys + num_lions + num_pandas + num_dogs
    result = total_animals
    return result

print(solution())