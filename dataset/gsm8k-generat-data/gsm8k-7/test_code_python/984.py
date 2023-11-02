def solution():
    # Set the ratio of kangaroos to koalas
    kangaroo_koala_ratio = 5

    # Set the number of kangaroos present
    num_kangaroos = 180

    # Calculate the number of koalas present
    num_koalas = num_kangaroos / kangaroo_koala_ratio

    # Calculate the total number of animals present
    total_animals = num_kangaroos + num_koalas

    result = (num_kangaroos, num_koalas, total_animals)
    return result

print(solution())