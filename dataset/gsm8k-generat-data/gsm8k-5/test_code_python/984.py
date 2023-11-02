def solution():
    kangaroo_per_koala = 5  # Legoland has 5 kangaroos for each koala
    total_kangaroos = 180  # Legoland has 180 kangaroos

    # Calculate the number of koalas and kangaroos
    total_animals = total_kangaroos / kangaroo_per_koala  # Total animals is the sum of koalas and kangaroos
    total_koalas = total_animals - total_kangaroos  # Subtract the number of kangaroos to get the number of koalas

    # Calculate the total number of animals
    total_animals = total_koalas + total_kangaroos
    result = total_animals
    return result

print(solution())